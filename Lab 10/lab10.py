# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 16:09:14 2015

@author: Jack
"""
# Python Lab 10 assessed submission file. Start: 10.12.15. End: 10.12.15
# Import required functions:
import numpy as np
import scipy.optimize as scio
import pylab


def model(t, Ti, Ta, c):
    """Implements and returns the model equation for a cooling process
    given input parameters for time, initial temperature Ti,
    ambient temperature Ta, and a time constant c"""
    return 1.0*((Ti - Ta)*np.exp((-t / c)) + Ta)


def read2coldata(filename):
    """Scans a file given in the argument of a function with two columns and
    returns the values in each column as a numpy array."""
    data = open(filename)
    lines = data.read()
    splits = lines.split()
    data.close()
    leftcol = []
    rightcol = []
    for i in range(len(splits)):
        if i % 2 == 0:
            leftcol.append(splits[i])
        else:
            rightcol.append(splits[i])
    a = np.array(leftcol, np.float64)
    b = np.array(rightcol, np.float64)
    return a, b


def extract_parameters(ts, Ts):
    """Function that, given numpy arrays ts and Ts, can extract and return Ti,
    Ta and c for the given data."""
    def curvefitter(x, a, b):
        return a*np.exp(-b*x)

    """def curve_fitter(f, a, b, n, noiselevel):
    ydata = create_y(f, a, b, n, noiselevel)
    return scio.curve_fit(polyfit_2, np.linspace(a, b, n),
                          ydata)"""
    curves, curvep = scio.curve_fit(model, ts, Ts, (0, 150, 300))
    Ti, Ta, c = curves
    return curves


def plot(ts, Ts, Ti, Ta, c):
    """Input Parameters:

      ts : Data for time (ts)
                (numpy array)
      Ts : data for temperature (Ts)
                (numpy arrays)
      Ti : model parameter Ti for Initial Temperature
                (number)
      Ta : model parameter Ta for Ambient Temperature
                (number)
      c  : model parameter c for the time constant
                (number)

    This function will create plot that shows the model fit together
    with the data.

    Function returns None.
    """

    pylab.plot(ts, Ts, 'o', label='data')
    fTs = model(ts, Ti, Ta, c)
    pylab.plot(ts, fTs, label='fitted')
    pylab.legend()
    pylab.savefig('testcompare.pdf')


def sixty_degree_time(Ti, Ta, c):
    """Function which computes and returns the value of t for which the tea
    will have cooled to 60 degrees"""
    time = c*np.log((Ti - Ta)/(60 - Ta)) * 1.0
    return time


def lazyfunction(filename):
    """Runs ALL the functions! Returns"""
    a, b = read2coldata(filename)
    Ti, Ta, c = extract_parameters(a, b)
    plot(a, b, Ti, Ta, c)
    woo = sixty_degree_time(Ti, Ta, c)
    return Ti, Ta, c, woo
