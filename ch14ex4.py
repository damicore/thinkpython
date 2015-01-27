#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import string

def get_list_of(typ, directory = os.getcwd()):
    res = []
    for path in os.listdir(directory):
        absolute = os.path.join(directory, path)
        print(absolute)
        if os.path.isdir(absolute):
            return get_list_of(typ, absolute)
        elif os.path.isfile(path) and path.endswith(typ) == typ:
            print('entering if')
            print(path)
            res.append(path)
        else:
            print(path, 'not caught')
    return res

print(get_list_of('py', '/home/damian/Code'))
