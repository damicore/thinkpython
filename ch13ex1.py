#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import random

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

def words_total(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)

def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort(reverse = True)
    return t

def not_in_wordlist(hist, words):
    res = {}
    for word in hist:
        if word not in words:
            res[word] = [word]
    return res

def not_in_wordlist(hist, words):
    s1, s2 = set(hist), set(words)
    return s1 - s2

wl = wordlist()
words = wordlist('words.txt')

print('total words: ', words_total(wl), ' and different words: ', different_words(wl))

print('most common words: ')
for word in most_common(wl)[:10]:
    print(word)

print('the following words are not in the wordlist:')
print(not_in_wordlist(wl, words))
