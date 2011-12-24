#!/usr/bin/env python
# -*- coding: utf-8

def hello(name):
    print "Hello %s" % name

hello("World")

def hello_all(*names):
    print "Hello %s" % ", ".join(names)

hello_all("Graham", "John", "Terry", "Eric", "Terry", "Michael")

def hello_prefix(name, prefix="Hello"):
    print "%s %s" % (prefix, name)

hello_prefix("World")
hello_prefix("Verden", "Hallo")
