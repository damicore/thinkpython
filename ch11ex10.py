#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pronounce import read_dictionary

def rot_13(s, n=13):
    res = ''
    for c in s:
        start = ord('a')
        order = (ord(c) + n - start) % 26 + start
        res += chr(order)
    return res

def word_list():
    fin = open('words.txt')
    d = dict()
    for line in fin:
        word = line.strip()
        d[word] = True
    return d

def print_rotate(wl):
    for i in range(1, 14):
        for word in wl:
            if rot_13(word, i) in wl:
                print(word, rot_13(word))

def check_puzzler(d):
    wa = d[1:]
    wb = d[0] + d[2:]
    wc = d[:]
    if check_words(wa, wb, wc):
        if pron(wa) == pron(wb) and pron(wa) == pron(wc):
            return True

def pron(s):
    return c06d[s]

def check_words(wa, wb, wc):
    if wa in word_list() and wb in word_list() and wc in word_list():
        return True
    else: return False


c06d = read_dictionary()
wl = word_list()
for s in c06d:
    print(s)
    if check_puzzler(s):
        print(s, ' works alright! ')

#print(read_dictionary())
