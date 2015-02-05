#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Wobbler import *
from math import atan2, degrees
import math
import random

class Tagger(Wobbler):
    """later"""
    def __init__(self, world, speed = 1, clumsiness = 60, color = 'red'):
        Wobbler.__init__(self, world, speed, clumsiness, color)
        self.origin_x, self.origin_y = self.x, self.y

    def steer(self):
        """Post Condition: The turtle is always looking towards the origin point"""
        self.nearest_turtle()
        if self.distance(0, 0) >= 200:
            self.turn_towards()

        # Turn towards other turtles
        self.turn_towards()

    def away(self, x=0, y=0):
        """return degrees from one point to the other"""
        deltax = self.x - x
        deltay = self.y - y
        turn = atan2(deltay, deltax)
        return turn * 180 / math.pi

    def turn_towards(self, x=0, y=0):
        self.heading = self.away(x, y) + 180
        self.redraw

    def distance(self, x=0, y=0):
        dx = self.x - x
        dy = self.y - y
        return math.sqrt(dx**2 + dy**2)

    def nearest_turtle(self):
        turtles = self.world.animals
        for turtle in turtles:
            print(turtle.x, turtle.y)

world = make_world(Tagger)
print(world.grid_size())
world.mainloop()
