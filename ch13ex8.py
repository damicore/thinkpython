#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import random

def read_file(fdir = 'aristotle.txt'):
    fin = open(fdir)
    res = []

    skip_header(fin)
    for line in fin:
        if '***' in line:
            return res
        line = line.strip().lower()
        line = line.replace('-', ' ')
        words = line.split()
        for word in words:
            res.append(word)
    return res

def skip_header(fin, header = '***'):
    for line in fin:
        if header in line:
            break

def process_words(t, order = 2):
    res = {}
    i = 0
    while i < len(t) - order:
        if i <= order:
            pass
        elif i == len(t) - order -1:
            return res
        else:
            prefix = tuple(t[i-order:i])
            suffix = t[i]
            if prefix not in res:
                res[prefix] = [suffix]
            else:
                res[prefix].append(suffix)
        i += 1

def say(mdict, order = 2):
    text = []
    prefix = random.choice(list(mdict.keys()))
    text.extend(prefix)
    while '.' not in text[-1]:
        prefix = tuple(text[-order:])
        suffix = random.choice(mdict[prefix])
        text.append(suffix)
    return text

markovs_dict = process_words(read_file())
text = ''

for words in say(markovs_dict):
    text += ' ' + words
print(text)
