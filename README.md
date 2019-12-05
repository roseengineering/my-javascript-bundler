
You do not have to bundle your javascript code together
using cat or with super sophisticated bundlers.  This bundler
is far more simpler.

The bundler also supports ES6/ES2015 imports.  So you can
babelify the code and then use this bundler to bundle the
result. 

Imports of source code
in js/ or src/ will have their js/ or src/ prefix replaced
with a '/'.

If your vendor libraries are in vendor/ or node\_modules/, imports
of these files will have their their above prefixes dropped.

Relative module addressing is not supported.  All addressing must
be absolute.  Bundlejs.py requires python3 to run.  By default the
entry module is 'main.js' which resolves to /main as the import
name.  This can be changed using the -e option.

For example to bundle a web app you can use:

     python3 bundlejs.py vendor/*.js js/*.js js/**/*.js > main.js

The bundler can also be used for bundling a library together.
For example to bundle up a module you can use: 

     python3 bundlejs.py src/*.js src/**/*.js > library.js

For example, let's bundle the code in the repo's js directory.

```
::::::::::::::
js/iamglamorous.js
::::::::::::::
exports.default = "I am glamorous";

::::::::::::::
js/main.js
::::::::::::::
iamglamorous = require('/iamglamorous');
console.log(iamglamorous.default);
```

Now run the following and you get:

```
$ python3 bundlejs.py js/*.js | node
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
'/iamglamorous':function(require, module, exports){
exports.default = "I am glamorous";

},
'/main':function(require, module, exports){
iamglamorous = require('/iamglamorous');
console.log(iamglamorous.default);

},
})('/main');
```

Copyright 2017 roseengineering
