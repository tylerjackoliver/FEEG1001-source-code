

def average(a, b):
    """Compute and return the arithmetic mean of a and b"""
    return (a + b) * 0.5

def distance(a, b): 
    """Compute and return the distance between numbers a and b"""
    return abs(a - b)

def geometric_mean(a, b):
    """Compute and return the geometric mean of two numbers a and b"""
    return (a * b) ** 0.5

def pyramid_volume(A, h):
    """Compute and return the volume of a pyramid with base area A and height h"""
    effective_height = h / 3.0
    return effective_height * A
