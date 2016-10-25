# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:06:44 2015

@author: Jack
"""
# Lab Three assessed work, 13.10.15
# Import required modules
import math

# Begin assessed work


def swing_time(L):
    """Compute and return the swing time in seconds for a pendulum
    of length l"""
    g = 9.81
    return 2 * math.pi * ((L / g) ** 0.5)


def range_squared(n):
    """Compute and return a list [0, 1, 4, ..., (n-1)^2]"""
    mylist = list(range(0, n))
    return [i ** 2 for i in mylist]


def count(element, seq):
    """Count and return the number of times an element occurs in a sequence"""
    # for i, j in enumerate(seq):
    # if j == element:
    # return i
    mylist = list(seq)
    return mylist.count(element)
