#! /usr/bin/env python

def are_reverse(wa, wb):
    """takes two words and returns True if they are both reverse
    pairs of each other"""
    if len(wa) != len(wb):
        return False

    for i in range(len(wa)):

