#! /usr/bin/env python

import bisect

def are_reverse(wa, wb):
    """checks if wa and wb are reversepairs"""
    if len(wa) != len(wb):
        return False

    j = len(wb)-1
    for i in range(len(wa)):
        if wa[i] != wb[j]:
            return False
        print ('i = ', i, ', j = ', j)
        j -= 1
    return True

def in_bisect(word_list, word):
    i = bisect.bisect_left(word_list, word)
    if i != len(word_list) and word_list[i] == word:
        return True
    else:
        return False

def make_word_list():
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list

word_list = make_word_list()
for word in word_list:
    if
