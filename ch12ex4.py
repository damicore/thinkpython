#!/usr/bin/env python
# -*- coding: utf-8 -*-

def load_dict(f = 'words.txt'):
    wlist = {}
    fin = open('words.txt')

    for line in fin:
        word = line.strip().lower()
        wlist[word] = word

    return wlist

def signature(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t

def find_anagrams():
    wd = load_dict()

    anagrams = {}
    for word in wd:
        t = signature(word)

        if t not in anagrams:
            anagrams[t] = [word]
        else:
            anagrams[t].append(word)
    return anagrams

def print_anagrams(d):
    for key, val in d.items():
        print(key, val)

def order_anagrams(d):
    t = []
    for letters, wlist in d.items():
        t.append((len(wlist), letters, wlist))

    t.sort()

    for length, letters, wlist in t:
        if len(letters) == 8:
            print(letters, wlist)

order_anagrams(find_anagrams())
