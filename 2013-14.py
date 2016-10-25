# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 16:30:53 2015

@author: Jack
"""
# Script answer file for the 2013/14 Python Mid-Term Exam
# Space for importing modules:
import scipy
#


def separate(x, reverse=False):
    """Function that takes a list x and returns a tuple of two lists (x1, x2)
    such that x1 contains the odd entries and x2 contains the even entries.
    An optional boolean argument can return the lists in reverse order."""
    x1 = []   # Odd
    x2 = []   # Even
    for i in range(0, len(x)):
        if i % 2 == 0:
            x1.append(x[i])
        else:
            x2.append(x[i])
    if reverse is False:
        return x1, x2
    else:
        x2 = list(reversed(x2))
        x1 = list(reversed(x1))
        return x1, x2


def capitalise_names(n):
    """Returns a list with the first letter in each item capitalised."""
    return_names = []
    for word in n:
        FirstLetter = word[0].capitalize()
        wordAsList = list(word)
        wordAsList[0] = FirstLetter
        return_names.append("".join(wordAsList))
    return return_names


def count(s, chars):
    """Takes a string s and a list of characters chars and returns the number
    of times that the characters appear in s"""
    dictionary = {k: 0 for k in chars}
    for character in s:
        if character in chars:
            if character in dictionary:
                dictionary[character] += 1
            else:
                dictionary[character] += 0
    return dictionary


def trap_area(xs, ys):
    """Returns an estimate for the integral corresponding to tabulated points
    xs and ys using the trapezoidal rule."""
    a = 0.5*sum([(xs[i+1]-ys[i])*(ys[i+1]+ys[i]) for i in range(0, len(xs)-1)])
    return a


def intersection(line1, line2):
    """Takes the slope m and the constant c of a line of equation y=mx+c and
    returns a tuple of the coordinates of intersection x and y of the lines."""
    m1, c1 = line1[0], line1[-1]
    m2, c2 = line2[0], line2[-1]
    xcoord = (c2 - c1) / (m1 - m2)
    ycoord = m1 * xcoord + c1
    return xcoord, ycoord


def change_unit(d, unit1, unit2):
    """Returns the distance conversion of a distance d in unit1 to unit2
    where units are meter, inch or foot."""
    conversiondictionary = {'meter': 1.0, 'inch': 0.0254, 'foot': 0.3048}
    if conversiondictionary[unit1] < conversiondictionary[unit2]:
        return d*conversiondictionary[unit2]/conversiondictionary[unit1]
    else:
        return d*conversiondictionary[unit1]/conversiondictionary[unit2]


def logistic(N):
    returnlist = [0.5]
    numberlist = range(0, N)
    for i in numberlist:
        valprime = (11/3)*returnlist[i-1]*(1-returnlist[i-1])
        returnlist.append(valprime)
    return returnlist


def create_f(xn, fn):
    """Returns a quadratic interpolation function f(x)."""
    xn = scipy.array(xn)
    fn = scipy.array(fn)

    def f(x):
        newf = scipy.interpolate.interp1d(xn, fn, kind="quadratic")
        return newf(x)

    return f


def max_f(f, x0):
    """Returns the local maximum of a function given an initial guess x0 and
    function f."""
    import scipy.optimize
    return scipy.optimize.fmin(lambda x: -f(x), x0)


def find_max():
    """Finds and returns the position x of the maximum of a function"""
    import scipy as sc
    xn = sc.array([0, sc.pi / 6, sc.pi / 3, sc.pi / 2, 2 * sc.pi / 3,
                   5 * sc.pi/6, sc.pi])
    yn = sc.array([1, 1.15, 1.98, 14.134, 1.98, 1.15, 1])
    return max_f(create_f(xn, yn), sc.pi / 2)
