# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:56:08 2015

@author: Jack
"""
# Assessed file for Python Lab 5 - 2.11.15


def vector_product3(a, b):  # Function has been partly checked 2.11.15
    """Computes and returns the  vector product of two 3D vectors a and b"""
    s = [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] -
         a[1] * b[0]]
    return s


def seq_mult_scalar(a, s):
    """Multiplies and returns list elements a multiplied by a scalar s"""
    # for i in a:
    #    i = i * s
    return [i * s for i in a]


def powers(n, k):
    """returns the list [1,n,n^2,n^3,...,n^k] where k is an integer"""
    s = []
    # mylist = list(range(k+1))
    # s.extend(mylist)
    for i in range(0, k+1):
        s.append(n ** i)
    return s


def traffic_light(load):  # Function has been checked 2.11.15
    """Takes a floating point number load and returns a string depending on the
    value of load"""
    s = float(load)
    if s < 0.7:
        return "green"
    elif s >= 0.7 and s < 0.9:
        return "amber"
    else:
        return "red"
