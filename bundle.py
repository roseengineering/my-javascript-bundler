
import os
import sys
import re

entrypoint = '.'

def norm(path):
    name, ext = os.path.splitext(path)
    name = re.sub('^js/', './', name)
    name = re.sub('^src/', './', name)

    name = re.sub('^vendor/', '', name)
    name = re.sub('^node_modules/', '', name)
    name = re.sub('/index$', '', name)
    return name

############################

args = sys.argv[1:]
if len(args) > 1 and args[0] == "-e":
    entrypoint = args[1]
    args = args[2:]


sys.stdout.write("""\
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
""")

for filename in args:
    with open(filename, encoding='utf-8') as f:
        buf = f.read()
        sys.stdout.write("'%s':function(require, module, exports){\n" % norm(filename))
        sys.stdout.write(buf)
        sys.stdout.write("\n")    # just in case the last light is a comment
        sys.stdout.write("},\n")

sys.stdout.write("})('%s');\n" % entrypoint)

