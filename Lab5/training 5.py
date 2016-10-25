# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 17:12:24 2015

@author: Jack
"""
# Training file for the training5.py submission - 1.11.2015


def count_sub_in_file(filename, s):
    """Computes and returns the number of times a substring s occurs in a file
    'filename'"""
    s = open(filename, 'r').read().count(s)
    if s != 0:
        return s
    else:
        return -1


def count_vowels(s):
    """Computes and returns the number of vowels in a string s"""
    vowels = list('aeiouAEOIU')
    # fancy dictionary comprehension to build the basic dictionary:
    count = 0  # {v: 0 for v in vowels}
    print(count)
    data = s
    # ok iterate over the string
    for letter in data:
        # if the letter is a vowel, count it
            if letter in vowels:
                count += 1
    return(count)
