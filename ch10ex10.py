#! /usr/bin/env python

def bisect(t, w):
    """Search through a binary search"""
    if len(t) == 1 and t[0] != w:
        #print(t)
        ##print(t, w)
        print('error fata')
        return None
    length = len(t) // 2
    if w < t[length]:
        bisect(t[:length], w)
    elif w > t[length]:
        bisect(t[length:], w)
    elif w == t[length]:
        print('found ', t[length], ' = ', w)
        return None

t = []
fin = open('words.txt')
for line in fin:
    a = line.strip()
    t.append(a)
bisect(t, 'vamos')

