#!/usr/bin/env python
# -*- coding: utf-8

def print_args(function):
    def wrapper(*args, **kwargs):
        print 'Arguments:', args, kwargs
        return function(*args, **kwargs)
    return wrapper

def yell(text):
    print text.upper()
yell = print_args(yell)
yell("foo")

@print_args
def write(text):
    print text
write("bar")
