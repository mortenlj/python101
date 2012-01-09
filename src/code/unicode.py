#!/usr/bin/env python
# -*- coding: utf-8

unicode_word = u"blåbærsyltetøy"

print "== From unicode =="
print "repr  : %r" % unicode_word
print "utf-8 : %s" % unicode_word.encode("utf-8")
print "latin1: %s" % unicode_word.encode("latin1") # aka iso-8859-1

utf8_word = "blåbærsyltetøy"
print "== From utf-8 =="
print "repr  : %r" % utf8_word
print "utf-8 : %s" % utf8_word
print "latin1: %s" % utf8_word.decode("utf-8").encode("latin1") # aka iso-8859-1
