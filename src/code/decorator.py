#!/usr/bin/env python
# -*- coding: utf-8

def print_args(function):
    def wrapper(*args, **kwargs):
        print 'Arguments:', args, kwargs
        return function(*args, **kwargs)
    return wrapper

@print_args # "apply" the "decorator" print_args to this function
def yell(text):
    print text.upper()

yell("foo")
