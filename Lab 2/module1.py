#Training file for the second python Lab.
def box_volume(a, b, c):
    """Function to calculate and return the volume of a box with side lengths
       a, b, c"""
    return a * b * c * 1.0


def fall_time(h):
    """Function to compute and return the time to fall a distance h"""
    g = 9.81
    return ((2 * h)/(g)) ** 0.5


def interval_point(a, b, x):
    """If a, b are the start and end points of an interval, and c a fraction
    between 0 and 1 determining how far towards a to go, return the result of the function"""
    interval_length = abs(a - b)
    toward_a = x * interval_length * 1.0
    if a < 0 and b < 0 and a > b:
        return a - toward_a
    elif a > b:
        return a - toward_a
    else:
        return a + toward_a


def impact_velocity(h):
    """Return the velocity of an object that has fallen from a height h"""
    return (2 * 9.81 * h) ** 0.5


def signum(x):
    """Returns various numbers based on arbitrary whims"""
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1