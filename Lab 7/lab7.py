# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 17:08:50 2015

@author: Jack
"""
import math
# Importing previous function derivative() for use in new file
"""

Issues with current script:

- newton(...) no longer returns any value - is this as a result of task 2 or
is this a major code issue? MAJOR CODE ISSUE - CHECK FOR LOOP
- redundant code in terms of is_palindrome_OLD(...) - will keep in for sake of
revision
"""


def derivative(f, x, eps=0.000001):
    """Computes and returns a numerical approximation of the first derivative
    of the function f(x)"""
    central_plus = f(x + eps / 2)
    central_minus = f(x - eps/2)
    return ((central_plus - central_minus)/eps)


def newton(f, x, feps, maxit):
    """Computes and returns the Newton-Raphson approximation to a root x1. If
    no solution found after a set number of iterations, a RuntimeError is
    returned."""
    count = maxit
    while count > 0:
        while abs(f(x)) > feps:
            x = x - f(x)/derivative(f, x)
            count = count - 1
            if count == 0:
                break
        else:
            return x
    if count == 0:
        raise RuntimeError("Failed after %d iterations" % maxit)


def is_palindrome_OLD(s):
    """Computes and returns if a string s is a palindrome"""
    a = True   # Setting up Conditional bools
    b = False
    HalfPoint = len(s) / 2   # Defining the mirror-line of a string
    if len(s) == 0 or 1:   # Start by elimination of trivial cases
        return a
    else:   # Begin a for-loop of multiple elements about mirror-line
        for character in s:
            if len(s) == 2:
                if s[0] == s[1]:
                    return a
                else:
                    return b
            elif s[HalfPoint - (HalfPoint - s[character])] == s[HalfPoint + (
                   HalfPoint - s[character])]:
                return a
            else:
                return b


def is_palindrome_OLD2(s):
    """Computes and returns if a string s is a palindrome"""
    s = str(s)
    a = True
    b = False
    rev_string = reversed(s)
    if rev_string == s:
        return a
        print("Debugging: True!")
    else:
        return b
        print("Debugging: False!")


def is_palindrome(s):
    'checks if a word is a palindrome'
    word = []
    for i in s:
        word.append(i)

    if len(s) == 0 or len(s) == 1:
        return True

    # while len(s)!=0 or len(s) != 1:

    while len(word) != 0 or len(word) != 1:
        if word[0] == word[-1]:
            word.pop(0)
            word.pop(-1)
            if len(word) == 0 or len(word) == 1:
                return True
        else:
            return False

# Creation of functions for self-testing


def f(x):
    return x ** 2 - 2   # Root condition


def g(x):
    return math.sin(x) + 1.1   # No root condition!
