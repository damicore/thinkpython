#! /usr/bin/env python

def is_sorted(t):
    for i in range(len(t)):
        if i != 0:
            if t[i] < t[i-1]:
                return False
    return True

def is_anagram(sa, sb):
    if len(sa) != len(sb):
        return False
    for c in sa:
        if c not in sb:
            return False
    return True


t = ['a', 'b', 'c', 'dia', 'dedo']
sa = 'raaaa'
sb = 'arrrr'
print(sa, sb, ' = ', is_anagram(sa, sb))
#exec6 print(t, ' ',is_sorted(t))
