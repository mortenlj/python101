#!/usr/bin/env python
# -*- coding: utf-8

# A simple function
def hello(name):
    print "Hello %s" % name

hello("World")

# A function with varargs
def hello_all(*names):
    print "Hello %s" % ", ".join(names)

hello_all("Graham", "John", "Terry", "Eric", "Terry", "Michael")
