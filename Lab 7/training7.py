# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:33:53 2015

@author: Jack
"""
from collections import Counter


def count_chars(s):
    """Computes and returns the number of occurences of characters in a string
    s"""
    return Counter(s)


def derivative(f, x, eps=0.000001):
    """Computes and returns a numerical approximation of the first derivative
    of the function f(x)"""
    central_plus = f(x + eps / 2)
    central_minus = f(x - eps/2)
    return ((central_plus - central_minus)/eps)


def f(x):
    return x ** 2
