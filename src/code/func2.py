#!/usr/bin/env python
# -*- coding: utf-8

# A function with an optional paramter
def hello(salutation, name="World"):
    print "%s %s" % (salutation, name)

hello("Hello") # no second parameter, uses default value World
hello("Hi", "There")

# A function with varargs and variable keyword args
def many(*args, **kwargs):
    print "args: %r, kwargs: %r" % (args, kwargs)

many()
many(1, 2, first="one", second="two")

