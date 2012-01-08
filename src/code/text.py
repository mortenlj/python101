#!/usr/bin/env python
# -*- coding: utf-8

# printf-style formatting supported by syntax
print "| %2.2f | %05d | %-10s | %10s |" % (3.141592653589793, 42, "Foo", "Bar")

# "".format is a new, more expressive formatting method
print "| {0:2.3} | {2:10} | {1:05} | {3:>10} |".format(
                                        3.141592653589793, 42, "Foo", "Bar")
