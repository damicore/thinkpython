#!/usr/bin/env python
# -*- coding: utf-8 -*-

def word_list(textfile='words.txt'):
    res = {}
    for word in open(textfile):
        word = word.strip()
        res[word] = word
    return res

def children(s, wl):
    i = 0
    children = []
    while i < len(s):
        temp = s[:i] + s[i+1:]
        if temp in wl:
            children.append(temp)
        i += 1
    return children

def check_dict(s, wl, res = []):
    if len(s) == 1:
        return res
    else:
        for child in children(s, wl):
            res.append(child)
            return check_dict(child, wl, res) # por qué mierda el return
    return False

"""
def reducible(s):
    if len(s) == 1 and s in wl:
        return True
    for word in s:
        if word in wl:
            return reducible(children(word, wl))
"""

wl = word_list()
