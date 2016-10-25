# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 09:20:22 2016

@author: Jack
"""
# Mock 14/15 exam
# Import required functions:
import scipy.interpolate as scii
import numpy as np


def average_age(people):
    """Takes a list of tuples people and returns the average age of the
    people"""
    ages = []
    for i in people:
        ages.append(i[-1])
    ageav = 0
    for j in ages:
        ageav += j
    return float(ageav / len(ages))


def rectangle(p1, p2):
    """Takes tuples describing the corners of a rectangle and returns area, xc
    and yc."""
    x1, y1 = p1[0], p1[-1]   # Import x-coords from tuple
    x2, y2 = p2[0], p2[-1]
    xc = (x2 + x1) / 2.0
    yc = (y2 + y1) / 2.0
    area = float(abs(x2 - x1) * abs(y2 - y1))
    returndic = {'area': area, 'xc': xc, 'yc': yc}   # Set up return dictionary
    return returndic


def word_count(s):
    """Returns the number of words in a string s"""
    word = s.split()
    return len(word)


def long_word(s):
    """Returns the longest word in a string s."""
    words = s.split()   # Create a list containing each word
    longest = words[0]   # Set first word to be longest
    for i in words:   # Iterate through list
        if len(i) > len(longest):
            longest = i   # If length of i > length longest, i = longest
    return longest


def shift(a):
    """Takes a list a as an argument and returns a list b with each element
    in a shifted by one place to the right in the list."""
    b = []
    for i in range(0, len(a)):
        b.append(a[i-1])
    return b


def rotate(a, n=1):
    """Applies shift(a) multiple times to rotate list elements and returns the
    result."""
    iters = 0   # Initialise value for iteration counter
    while iters < n:
        b = []
        for i in range(0, len(a)):
            b.append(a[i-1])   # Perform shift function
        iters += 1   # Add one to iteration count
        a = b   # Set a to b to ensure function can be run again
    return a


def power(In, Vn):
    """Takes lists of measured currents and voltages and returns a list
    containing the electric power P = VI corresponding to each measurement."""
    powervals = []
    if len(In) == len(Vn):
        for i in range(0, len(In)):
            powervals.append(In[i] * Vn[i])
        return powervals
    else:
        print("The lists are not of the same length - function failed.")


def active(In, Vn):
    """Computes and returns a list of values for which the circuit is active"""
    powervals = power(In, Vn)
    activevals = []
    for i in powervals:
        if i < 0:
            activevals.append(i)
    return activevals


def interp_V(In, Vn):
    """Returns a function f which calculates the inteprolated value of the
    voltage V for a current I."""
    In, Vn = np.array(In), np.array(Vn)   # scii requires array-like inputs
    f = scii.interp1d(In, Vn)
    return f


def T_iteration(n):
    """Calculates the approximate solution to the temperature of an object
    using an iteration scheme and returns a list of the temperatures for given
    times."""
    T = list(range(0, n+1))
    T[0] = 1
    for i in range(0, n):
        ti = float(i / n)
        T[i+1] = T[i] + (1.0/n) * (-2*T[i] + 0.5*np.exp(-ti))
    return T


def T_error(n):
    tinterp = T_iteration(n)
    Te = []
    for i in range(0, n+1):
        ti = float(i / n)
        Tex = 0.5*np.exp(-2*ti) + 0.5*np.exp(-ti)
        abserr = tinterp[i]
        T = abserr - Tex
        Te.append(abs(T))
    return max(Te)
