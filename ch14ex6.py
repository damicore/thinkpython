#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib

conn = urllib.urlopen('http://thinkpython.com/secret.html')
for line in conn:
    print(line.strip())
