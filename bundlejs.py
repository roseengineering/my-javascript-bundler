#!/usr/bin/python3

import os, sys, re

entry = '/main'

def norm(path):
    name, ext = os.path.splitext(path)
    res = name
    if name == res: name = re.sub('^js/', '/', name)
    if name == res: name = re.sub('^src/', '/', name)
    if name == res: name = re.sub('^vendor/', '', name)
    if name == res: name = re.sub('^node_modules/', '', name)
    if name == res: name = re.sub('^([^/])', '/\\1', name)
    return name

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

for filename in sys.argv[1:]:
    with open(filename, encoding='utf-8') as f:
        buf = f.read()
        sys.stdout.write("'%s': " % norm(filename))
        sys.stdout.write("function(require, module, exports){\n")
        sys.stdout.write(buf)
        sys.stdout.write("\n")    # in case the last line is a comment
        sys.stdout.write("},\n")

sys.stdout.write("})('%s');\n" % entry)

