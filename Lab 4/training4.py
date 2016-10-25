# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 15:28:37 2015

@author: Jack
"""
from urllib.request import urlopen

# Training file for the Python Lab 4


def line_averages(filename):
    """Computes and returns the mean of lines of a data file"""
    f = open('filename', 'r')
    DataList = []
    for line in f:
        data = line.split(',')
        total = 0
        for s in data:
            total += int(s)
        mean = total / len(s)
        DataList.append(mean)
    return DataList


def noaa_string():
    url = "http://weather.noaa.gov/pub/data" +\
        "/observations/metar/decoded/EGHI.TXT"
    noaa_data_string = urlopen(url).read()
    return noaa_data_string


def noaa_temperature(s):
    """Returns the temperature of Southampton from the NOAA website"""
    s = str(noaa_string(), 'UTF-8')
    temperature_location = s.find(('Temperature'))
    # if s[temperature_location] == ' ':
    # temperature = s[temperature_location+19:temperature_location:20]
    # else:
    # temperature = s[temperature_location+19: temperature_location:21]
    temperature = s[temperature_location+19:temperature_location+21]
    temperature.strip()
    return temperature
