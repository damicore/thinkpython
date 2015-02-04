#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Wobbler import *
from math import atan2

class Tagger(Wobbler):
    """later"""
    def __init__(self, world, speed = 1, clumsiness = 60, color = 'red'):
        Wobbler.__init__(self, world, speed, clumsiness, color)
        self.origin = (self.x, self.y)

    def steer(self):
        """a"""
        print(self.origin)

make_world(Tagger)
