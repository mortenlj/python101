#!/usr/bin/env python
# -*- coding: utf-8

def make_type(type_name, attributes):
    return type(type_name, (object,), attributes)

tags = [("b", {}), ("img", {"src": "http://url.com/img.jpg", "alt": "An image"})]
for name, attributes in tags:
    t = make_type(name, attributes)
    print t, ["%s: %s" % (key, getattr(t, key)) for key in t.__dict__ if not key.startswith("__")]
