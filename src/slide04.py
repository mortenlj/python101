#!/usr/bin/env python
# -*- coding: utf-8

print "Utstrakte muligheter for formattering av tekst"
print "| %2.2f | %05d | %-10s | %10s |" % (3.141592653589793, 42, "Hei", "Hopp")

print "En nyere formatterings funksjon som kan gjøre enda mer"
print "| {0:2.3} | {2:10} | {1:05} | {3:>10} |".format(3.141592653589793, 42, "Hei", "Hopp")
