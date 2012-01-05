#!/usr/bin/env python
# -*- coding: utf-8

def simple_gen(start=0, step=1):
    while start < 10:
        yield start
        start += step

for i in simple_gen():
    print i,
print

for i in simple_gen(5, 2):
    print i,
print
