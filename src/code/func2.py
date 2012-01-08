#!/usr/bin/env python
# -*- coding: utf-8

# A function with varargs and keyword args
def many(*args, **kwargs):
    print "args: %r, kwargs: %r" % (args, kwargs)

many()
many(1, 2, first="one", second="two")

# A function with an optional paramter
def hello(prefix, name="World"):
    print "%s %s" % (prefix, name)

hello("Hello")
hello("Hi", "There")
