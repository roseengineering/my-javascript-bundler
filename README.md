
Gone are the days when you can bundle your javascript code together
using cat.  Now far more sophisticated bundlers are required.
However if you want a middle ground you can try my bundler in this repo.
The bundler supports ES6/ES2015 imports.  It resembles sstephenson/stitch
more than browserify.  

Your source code should be in js/ or src/.  Imports of source code
modules in js/ or src/ should be prefixed with './'.  Your vendor modules
should be in vendor/ or node_modules/.  Imports of vendor modules
are not prefixed.

Relative module addressing is not supported.  All addressing must
be absolute.  If the module's name ends in /index, this suffix will be
stripped.  Also bundle.py requires python3 to run.  By default the
entry module is '.' which resolves to index.js.  This can be changed using the -e option.

For example to bundle a web app you can use:

     python3 bundle.py vendor/*.js js/*.js js/**/*.js > index.js

The bundler can also be used for bundling vendor modules together.
For example to bundle up a module you can use: 

     python3 bundle.py src/*.js src/**/*.js > module.js

In other words, all bundles can be rebundled.

Now, let's bundle the example in the repo's js directory.

```
::::::::::::::
js/iamglamorous.js
::::::::::::::
exports.default = "I am glamorous";

::::::::::::::
js/index.js
::::::::::::::
iamglamorous = require('./iamglamorous');
console.log(iamglamorous.default);
```

Now run the following and you get:

```
~/my-javascript-bundler $ python3 bundle.py js/*.js | node
I am glamorous
```

The full bundled result is shown below:

```
var module = module || {};
module.exports = (function bundler(modules){
    var cache = {};
    return function require(name){
        var m, e = cache[name];
        if(!e && modules[name]){
            m = { exports: {} };
            modules[name].call(null, require, m, m.exports, bundler, modules);
            e = cache[name] = m.exports;
        }
        return e;
    }
})({
'./iamglamorous':function(require, module, exports){
exports.default = "I am glamorous";

},
'.':function(require, module, exports){
iamglamorous = require('./iamglamorous');
console.log(iamglamorous.default);

},
})('.');
```

Copyright 2017 roseengineering
