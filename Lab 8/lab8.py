# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:02:14 2015

@author: Jack
"""
# Lab file for FEEG1001 Python Lab 8
import numpy as np
import pylab  # Importing functions
import scipy.optimize


def f1(x):
    """Computes and returns the value of f1 given an argument x"""
    f = np.cos(2*np.pi*x)*np.exp(-(x ** 2))   # Define formula
    return f   # Return value


def f2(x):
    """Computes and returns the value of f2 given an argument x"""
    f = np.log(x + 2.1)   # Define formula
    return f   # Return value


def create_plot_data_(f, xmin, xmax, n):
    """Computes and returns the range ys mapped by a function f from a domain
    xs"""
    xs = []
    ys = []
    count = 0
    for i in range(xmin, n):   # Setting up the x formula
        xs.append(xmin + count * ((xmax - xmin) / (n - 1)))
        count += 1
    for j in xs:
        ys.append(f(j))
    return xs, ys


def myplot():
    """Computes and returns None and a graph of two functions f1 and f2"""
    xmax = 2
    xmin = -2
    n = 1001

    def graph1(n):
        x = np.linspace(xmin, xmax, n)
        y1 = f1(x)
        return x, y1

    def graph2(n):
        x = np.linspace(xmin, xmax, n)
        y2 = f2(x)
        return x, y2

    x, y1 = graph1(n)
    x, y2 = graph2(n)
    pylab.plot(x, y1, label='f1(x)')
    pylab.plot(x, y2, label='f2(x)')
    pylab.legend()
    pylab.xlabel('x')
    pylab.ylabel('y')
    pylab.savefig('plot.png')
    pylab.savefig('plot.pdf')
    pylab.show()
    return None


def find_cross():
    """Computes and returns the intersection of two functions f1 and f2"""
    def f(x):
        return f1(x) - f2(x)

    return scipy.optimize.brentq(f, 0.102, 0.104)

# Programs for testing


def f(x):
    """Computes and returns x multiplied by 10 for the purpose of testing."""
    return x * 10


def create_plot_data(f, xmin, xmax, n):
    """Computes and returns a tuple (xs, ys) where xs and ys are two sequences,
    each containing n numbers"""
    xs = []
    ys = []
    for i in range(n):
        xi = xmin + i * (xmax - xmin) / (n-1.0)
        xs.append(xi)
    for y in xs:
        result = f(y)
        ys.append(result)
    return (xs, ys)
