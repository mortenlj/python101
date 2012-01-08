#!/usr/bin/env python
# -*- coding: utf-8

# Import a module or package, get access to all names in module
import os.path
print [x for x in dir(os.path) if not x.startswith("_")]

# Import a specific name from module into own namespace
from os.path import abspath
path = abspath("import_modules.py")
print path

# Import specific name, giving it new name in own namespace
from os.path import basename as bs
print bs(path)
