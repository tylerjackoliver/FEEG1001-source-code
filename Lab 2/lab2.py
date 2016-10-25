# Lab 2 submission - Jack Tyler 12.10.15
# Remember PEP-8: no trailing whitespaces and correct grammar usage 
# at all times
# Remember to double check and triple check outputs
# No more than 72 characters per line
# Double spaces between major elements of the code
def seconds2days(n):
	"""Compute and return the number of days that corresponds to n
    seconds"""
	float_convert = n * 1.0 #Ensure output is floating point
	return float_convert / (60 * 60 * 24) #1 day is 60*60*24 seconds


def box_surface(a, b, c):
	"""Compute and return the surface area of a cuboid with edge
    lengths a, b and c"""
	faces_ab = a * b * 2
	faces_ac = a * c * 2
	faces_bc = b * c * 2
	return faces_ab + faces_bc + faces_ac


def triangle_area(a, b, c):
	"""Compute and return the area A of a triangle with edge lengths a,
    b and c"""
	s = (a + b + c) / 2.0
	A = (s * (s - a) * (s - b) * (s - c)) ** 0.5
	return A


#End of assignment