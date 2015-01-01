#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

def wordlist(fdir = 'aristotle.txt'):
    res = dict()
    fin = open(fdir)
    beg = True
    for line in fin:
        if line[:3] == '***':
            if beg == True:
                res = {}
                beg = False
            elif beg == False:
                break
        words = line.split(' ')
        for word in words:
            word = word.strip(string.whitespace + string.punctuation).lower()
            res[word] = res.get(word, 0) + 1
    return res

def count_vocab(wl):
    res = {}
    for word in wl:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    return res

wl = wordlist()
print(wl)
