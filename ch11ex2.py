#! /usr/bin/env python

def histogram(s):
    """makes a histogram"""
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def histogram_(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def print_hist(h):
    """wa?"""
    ordered = sorted(h.keys())
    for c in ordered:
        print(c, h[c])

def reverse_lookup(d, v):
    tofk = []
    for k in d:
        if d[k] == v:
            tofk.append(k)
    return tofk

print(reverse_lookup(histogram_('troglodita'), 1))
