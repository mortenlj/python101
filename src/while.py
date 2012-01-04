#!/usr/bin/env python
# -*- coding: utf-8

starting_seconds = 2151
seconds = starting_seconds
minutes = 0
while seconds > 60:
    minutes += 1
    seconds -= 60
print "%d seconds = %d minutes and %d seconds" %\
                    (starting_seconds, minutes, seconds)
