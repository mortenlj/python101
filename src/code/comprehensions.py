#!/usr/bin/env python
# -*- coding: utf-8

numbers = (1,2,3,4,5)

quads = [i*i for i in numbers]
print quads

even_quad_lookup = dict( (i,i*i) for i in numbers if i % 2 == 0 )
print even_quad_lookup
