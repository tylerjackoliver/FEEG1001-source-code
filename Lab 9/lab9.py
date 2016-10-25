# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 18:17:36 2015

@author: Jack
"""
# Python Lab 9 file.
import scipy.integrate
import scipy.stats
# Import previous function


def trapez(f, a, b, n):
    """Approximates and returns the definite integral of f from a to b by
    the composite trapezoidal rule, using n subintervals"""
    aprime = float(a)
    bprime = float(b)
    nprime = float(n)
    h = (bprime - aprime) / nprime
    s = f(aprime) + f(bprime)
    for i in range(1, n):
        s += 2 * f(aprime + i * h)
    return s * h / 2.0


def finderror(n):
    """Returns the error in computing int(x**2) via the trapezium rule."""
    def f(x):
        return x**2
    trapezium = trapez(f, -1, 2, n)

    def intvalue(x):
        return (x**3)/3.0

    num = intvalue(2) - intvalue(-1)
    serror = float(num - trapezium)
    return serror


def using_quad():
    """Uses scipy.integrate to return the approximate value of an integral
    of function j"""
    def j(x):
        return x**2

    return scipy.integrate.quad(j, -1.0, 2.0)


def std_dev(x):
    """Computes and returns the corrected sample standard deviation from a set
    of numbers x"""
    mu = sum(x)/len(x)
    sumnum = 0.0
    for i in x:
        i = (i - mu) ** 2.0
        sumnum += i
    sigmasquare = (1.0 / (len(x) - 1.0)) * sumnum
    return sigmasquare ** 0.5


def std_dev_checker(x):
    """Piece of code designed to test and return the same value of
    std_dev(x)"""
    return scipy.stats.tstd(x)


def checkers(x):
    """Checks the values of _checker and _std_dev are the same and returns an
    appropriate result"""
    if std_dev(x) == std_dev_checker(x):
        return "Success! I think it works!"
    else:
        return "Error!"
        print("Std_dev gave " + std_dev(x))
        print("Std_dev_checker" + std_dev_checker(x))
