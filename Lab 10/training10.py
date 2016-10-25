# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 11:07:07 2016

@author: Jack
"""
import numpy as np


def model(t, Ti, Ta, c):
    """Implements and returns the model equation for a cooling process
    given input parameters for time, initial temperature Ti,
    ambient temperature Ta, and a time constant c"""
    Ti = float(Ti)
    Ta = float(Ta)
    c = float(c)
    return 1.0*((Ti - Ta)*np.exp((-t / c)) + Ta)
