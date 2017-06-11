
Gone are the days when you can bundle your javascript code together
using cat.  Now much more sophisticated bundlers are required.
However if you want a middle ground you can try my bundler in this repo.
The bundler supports ES6/ES2015 imports.  It resembles sstephenson/stitch
more than browserify.  

Your source code should be in js/.  Any imports of source code
modules should be prefixed with './'.  Your vendor modules
should be in src/, vendor/ or node_modules/.  Imports of vendor modules
should not be prefixed with './' or '/'.

Relative module addressing is not supported.  All addressing must
be absolute.  If the module's name ends in /index, this suffix will be
stripped.  Also bundle.py requires python3 to run.  By default the
entry module is 'main'.  This can be changed using the -e option.

For example to bundle a web app you can use:

     python3 bundle.py vendor/*.js js/*.js js/**/*.js > index.js

The bundler can also be used for bundling modules which can
then copied to the vendor/ directory and used like vendor modules.

For example to bundle up a module you can use: (The entry point is changed
to 'index' from the default 'main')

     python3 bundle.py -e index src/*.js src/**/*.js > module.js

Copyright 2017 roseengineering
