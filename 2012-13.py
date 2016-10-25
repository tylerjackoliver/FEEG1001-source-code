# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 13:09:32 2015

@author: Jack
"""
# Answer script to the 2012/13 Python exam - 17.12.2015
import scipy.interpolate
import numpy


def mult3vec(c, v):
    """Returns the product of three vectors v1, v2 and v3 multiplied by a
    scalar c"""
    for i in v:
        i = c * i
    return v


def multvec(c, v):
    """Returns the product of n vectors v1, v2...vn multiplied by a scalar c"""
    for i in v:
        i = c * i
    return v


def convert_time(t):
    """Returns the number of days, hours and minutes in a value of minutes t"""
    secs = 60 * t
    minutes = int(secs / 60) % 60
    hours = int(secs / 3600)
    days = int(secs / (3600*24))
    return days, hours, minutes


def nearest(xs, a):
    """Returns the element of xs that is nearest to a"""
    value_list = []
    for i in xs:
        value_list.append(abs(i - a))
    mini = min(value_list)
    for j in xs:
        if mini + a == j:
            return j
        elif mini * -1 + a == j:
            return j
        else:
            pass


def derivative(f, xs):
    """Approximates and returns the derivative of a function f at points in
    xs"""
    delta = 10 ** -6
    returnlist = []
    for i in xs:
        f1 = f(i + delta)
        f2 = f(i)
        returnlist.append((f1 - f2) / delta)
    return returnlist


def read(filename):
    """Reads and returns a tuple of two lists the data of a file filename"""
    data0 = open(filename)
    data1 = read(data0)
    data0.close
    data1.split(',')
    print(data1)


def isfib(F):
    """Returns true and false given a list F whether or not it is a Fibonacci
    sequence"""
    if len(F) < 2:
        return False
    elif F[0] == 0 and F[1] == 1:
        for i in range(2, len(F)):
            if F[i] == F[i - 1] + F[i - 2]:
                return True
            else:
                return False
    else:
        return False


def f_from_data(xs, ys):
    """Returns a bunch of stuff"""
    ys_array = numpy.array(ys)

    def returner(x):
        return x

    def f(x):
        for i in xs:
            if x == i:
                return ys[i]
            else:
                newval = scipy.interpolate.interp1d(nearest(xs, x), ys_array)
            return newval
    return f(x)
