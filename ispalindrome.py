#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_palindrome(s):
    print(s)
    if len(s) <= 1:
        return True

    if s[0] == s[-1]:
        print (s[0], ' ', s[-1])
        return is_palindrome(s[1:-1])
    elif s[0] != s[-1]:
        print('about to return false')
        return False

print(is_palindrome('gultug'))
