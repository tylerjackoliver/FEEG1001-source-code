# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:12:17 2015

@author: Jack
"""

# Class notes for FEEG1001 numerical methods Lecture 4

# To integrate a function, use SciPy:

import scipy


def integrator(f, a, b):
    integral = scipy.integrate.quad(f, a, b)
    return integral

# If we don't know the function, just data points, but still want to integrate:
# Use of numerical method, eg trapezium rule, assumigng a linear relationship
# between each data point:


def intergrator_numerical(xs, ys, strips):
    