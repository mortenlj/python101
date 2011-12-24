#!/usr/bin/env python
# -*- coding: utf-8


# En funksjon med varargs og kw-args
def many(*args, **kwargs):
    print "args: %r, kwargs: %r" % (args, kwargs)

many()
many(1, 2, first="one", second="two")

# En funksjon med valgfritt parameter
def hello(prefix, name="World"):
    print "%s %s" % (prefix, name)

hello("Hello")
hello("Hallo", "Verden")
