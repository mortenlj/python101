#!/usr/bin/env python
# -*- coding: utf-8

FILENAME = "no-such-file"

try:
    fobj = open(FILENAME)
except IOError as e:
    print "Oops: %s" % e
else:
    print "Someone has created the file %r O_o" & FILENAME
