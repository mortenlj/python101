#!/usr/bin/env python
# -*- coding: utf-8

# En enkel funksjon
def hello(name):
    print "Hello %s" % name

hello("World")

# En funksjon med varargs
def hello_all(*names):
    print "Hello %s" % ", ".join(names)

hello_all("Graham", "John", "Terry", "Eric", "Terry", "Michael")
