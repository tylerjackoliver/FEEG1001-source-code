# Lab 3 Training File
import math


def degree(x):
    """Calculate and return the equivalent measurement in degrees of
    x radian"""
    return (x * 360.0)/(2 * math.pi)  # Ensuring floating point whilst
# applying formula


def min_max(x):
    """Return the minimum and maximum values in a list"""
    return (min(x), max(x))


def geometric_mean(x):
    """Return the geometric mean of two items in a list"""
    return (x[0] * x[1]) ** 0.5
