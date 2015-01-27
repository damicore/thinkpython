#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class point(object):
    """
    doc
    """

def distance_between_points(p1, p2):
    """
    docstring
    """
    b = p1.x - p2.x
    h = p1.y - p2.y
    distance = math.sqrt(b**2 + h**2)
    return distance

blank = point()
blank.x, blank.y = 4, 5
blank.corner = point()
blank.corner.x = 5
blank.corner.y = 10
p = point()
p.x, p.y = 7, 9

print(distance_between_points(p, blank))
print(blank.corner.y)

class time(object):
    """tiempo capo"""
    def __init__(self, hour=0, minute=0, second=0):
        super(time, self).__init__()
        self.hour, minute, second = hour, minute, second
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    def __add__(self, other):
        """docstring for __add__"""
        return self + other
