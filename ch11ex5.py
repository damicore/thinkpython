#!/usr/bin/env python

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def invert_dict(d):
    """docstring for invert_dict"""
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
        return inverse

known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

def ack(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m,n-1))

print(ack(10,5))
