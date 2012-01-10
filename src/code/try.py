#!/usr/bin/env python
# -*- coding: utf-8

FILENAME = "no-such-file"

try:
    fobj = open(FILENAME)
except IOError as e:
    print "Oops: %s" % e
finally:
    print "Finally out of there"
