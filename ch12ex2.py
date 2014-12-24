#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import random

def unstable_sort(words):
    t = []
    for word in words:
        t.append((len(word), random(), word))

    t.sort(reverse=True)

    res = []
    for length, i, word in t:
        res.append(word)
    return res

words = ['hola', 'casa', 'cosa', 'ah', 'espiraladisimo']
sortd = unstable_sort(words)
for i in sortd:
    print(i)
