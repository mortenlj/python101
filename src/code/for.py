#!/usr/bin/env python
# -*- coding: utf-8

numbers = (1,2,3,4)
for i in numbers:
    print i,
print

for i in numbers:
    if i == 5: break
else:
    print "Did not find 5 in numbers"

for i in numbers:
    if i == 3: break
else:
    print "Did not find 3 in numbers"

