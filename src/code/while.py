#!/usr/bin/env python
# -*- coding: utf-8

seconds = starting_seconds = 2151
minutes = 0

while seconds > 60:
    minutes += 1
    seconds -= 60

print "%d seconds = %d minutes and %d seconds" %\
                    (starting_seconds, minutes, seconds)
