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

def check_dict(s, wl, res = [], called = 0):
    if len(s) == 1 and s in wl:
        res.append(s)
        return res
    else:
        for child in children(s, wl):
            print(res,'call number ', str(called), 'with s = ', s) #
            res.append(child)
            check_dict(child, wl, res, called+1)

def reducible(t):
    global wl
    print(wl)
    for word in t:
        if word in wl:
            return reducible(children(word))

wl = word_list()
print(check_dict('sprite', wl))
