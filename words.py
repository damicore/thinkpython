#!/usr/bin/env python2

tcount = 0
noecount = 0

def has_no_e(word):
    for char in word:
        if char == 'e':
            return False
    return True

def avoids(word, letters):
    for char in word:
        for forbid_let in letters:
            if char == forbid_let:
                return False
    return True

#fin = open('words.txt')
#for line in fin:
    #word = line.strip()
    #if has_no_e(word):
        #print word

print(avoids('caca', 'dfdfd'))
