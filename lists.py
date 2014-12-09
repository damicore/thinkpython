#! /usr/bin/env python2

def flatten_list(nested, newlist = []):
    for element in nested:
        if type(element) == list:
            flatten_list(element, newlist)
        else:
            newlist.append(element)
    return newlist

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res
listai = [ 1, 2,[3, 4], 5, [6, [7, 8]]]
lista_s = ['hola', 'QuiEn', [['sos'], 'Y']]
