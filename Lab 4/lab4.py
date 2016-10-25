# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 11:05:47 2015

@author: Jack
"""
# Lab 4 submission for FEEG1001: 27.10.15


def seq_sqrt(xs):
    """Computes and returns the square root of every element in a list"""
    return [i ** 0.5 * 1.0 for i in xs]


def mean(xs):
    """Compute and return the arithemetic mean of three numbers in a list"""
    total = 0.0  # Initialise value of total and ensure it is a float
    for i in xs:  # Iterate through file to add to variable total
        total += i
    quotient = len(xs)
    return total/quotient


def wc(filename):
    """Computes and returns the number of words in a file"""
    textfile = (open(filename, 'r+'))
    wordcount = 0  # Initialise value of wordcount
    for line in textfile:  # Iterate through file
        wordcount += len(line.split())  # Add to wordcount the value of the
        # split of each line
    return wordcount
