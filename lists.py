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

def cumulative(t):
    lst = t[:]
    for i in range(len(t)):
        if i != 0:
            lst[i] += lst[i-1]
    return lst

def middle(t):
    start = 1
    end = len(t) - 1
    return t[start:end]

def chop(t):
    del t[len(t)-1]
    del t[0]
    return None

listain = [1, 2, 3, 4]
listai = [ 1, 2,[3, 4], 5, [6, [7, 8]]]
lista_s = ['hola', 'QuiEn', [['sos'], 'Y']]

print(cumulative(listain))
print middle(listain)
print(listain)
chop(listain)
print(listain)
