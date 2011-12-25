#!/usr/bin/env python
# -*- coding: utf-8

class Indent(object):
    def __init__(self, indent=4):
        self.indent = indent

    def _indent(self):
        return " "*self.indent

    def output(self, msg):
        print "%s%s" % (self._indent(), msg)

i4 = Indent()
i4.output("Test")
i2 = Indent(2)
i2.output("Test")

