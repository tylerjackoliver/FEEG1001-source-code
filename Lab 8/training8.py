# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 11:04:48 2015

@author: Jack
"""

# Jack Tyler Training 8 Python file for FEEG1001: Start 19.11.15, End:

####################################################################

# BEGIN TASK

####################################################################
import math as m   # Import required packages
from six import iteritems


    def f1(x):
        """Computes and returns the value of f1 given an argument x"""
        f = m.cos(2*m.pi*x)*m.exp(-(x ** 2))   # Define formula
        return f   # Return value
    
    
    def f2(x):
        """Computes and returns the value of f2 given an argument x"""
        f = m.log(x + 2.1)   # Define formula
        return f   # Return value


def positive_places(f, xs):
    """Taking arguments as a function f and some list of numbers xs,
    return only those numbers for which f is greater than 0 without
    the use of a for-loop"""
    # mapping = map(f, xs)
    # return_list = filter(lambda a: a > 0, mapping)
    # return return_list
    return [x for x in xs if f(x) > 0]


def reverse_dic(d):
    """Compute and return the reverse of a dictionary d: ie, the
    key k and associated value v becomes the key v and associated
    value k"""
    # inv_dic = {v: k for k, v in d}   # v is k for k, v in d
    res = dict((v, k) for k, v in iteritems(d))
    return res


def simple_function(x):
    return x ** 3

mylist = {"a": 2, "b": 3, "cow": "moo", "yay": "poo"}
