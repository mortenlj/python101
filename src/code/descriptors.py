#!/usr/bin/env python
# -*- coding: utf-8
class Final(object):
    def __init__(self):
        self.val = 10
    def __get__(self, obj, objtype):
        return self.val
    def __set__(self, obj, val):
        raise AttributeError("Not allowed")

class MyClass(object):
    x = Final()

m = MyClass()
print m.x
try:
    m.x = 20
except AttributeError as e:
    print e
print m.x
