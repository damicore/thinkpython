#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sumall(*args):
    """sums a variable length tupple"""
    res = 0
    for i in args:
        res += i
    return res

print(sumall(1, 2, 3))
