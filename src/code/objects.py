#!/usr/bin/env python
# -*- coding: utf-8

a_number = 123
a_float = 3.141592653589793
a_string = "   this has spaces at the start"

print "%04d, %2.2f, %s" % (a_number, a_float, a_string)
print "%04d, %2.2f, %s" % (a_number, a_float, a_string.strip())
print "Bits needed to represent %d in binary: %d" % (a_number, a_number.bit_length())
print "Pnrfne pvcure".encode("rot13")
