%Python Lecture 1
%-----------------------------
%Covering types of variable; float/complex/string and type() command
%-----------------------------
a = 1 + 4j %Complex
type(a)
b = "Hello" %String
type(b)
%-----------------------------
%Use of dir() to list variables/functions
%-----------------------------

%BREAK - Moving on to defining functions

def get_average(a, b):
	return (a+b)/2
	
def distance(a, b):
	return a - b

key = [1, 4, 6, 4, 8, 3]

for num in key:
	return num*2

%Basics on docstrings - """ ... """
	
