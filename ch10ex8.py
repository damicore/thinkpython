#! /usr/bin/env python

import random

def remove_duplicates_no(t):
    res = []
    for i in range(len(t)):
        for y in range(len(t)):
            if i != y and t[i] != t[y] and t[i] not in res:
                res.append(t[i])
    return res

def remove_duplicates(t):
    if len(t) == 0:
        return t
    t = sorted(t)
    for i in range(len(t)):
        if t[i] == t[i - 1]:
            t.remove(t[1])
            remove_duplicates(t)

def has_duplicates(t):
    for i in range(len(t)):
        for y in range(len(t)):
            if i != y and t[i] == t[y]:
                return True
    return False

t = ['a', [5, 6], 1, 'ba', [5, 6]]

def random_birthdays(n):
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t

def count_matches(students, samples):
    matches = 0
    for i in range(samples):
        t = random_birthdays(students)
        if has_duplicates(t):
            matches += 1
    return matches

t = [3,1,2,3,3,4,5,6,6,6]
#ex8 print(count_matches(23, samples)/samples*100, '% of probabilities')
print(t, ' -> ', remove_duplicates_no(t))
