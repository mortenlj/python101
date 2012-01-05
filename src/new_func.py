#!/usr/bin/env python
# -*- coding: utf-8

def outer(first):
    def inner(second):
        print "%s %s" % (first, second)
    return inner

hello_func = outer("Hello")
hello_func("World")

outer("First")("Second")
