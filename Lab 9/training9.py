# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Python training file for lab 9.
# Start: 2.12.15. End:
from six import iteritems
"""Some support functions"""


def code0():
    """A trivial code - no change."""
    return {}


def code1():
    """A very simple example (symmetric)."""
    return {'e': 'x', 'x': 'e'}


def code2():
    """A simple example i->s, s->g and g->i."""
    return {'i': 's', 's': 'g', 'g': 'i'}


def code3():
    """A more complicated code."""
    dic = {}
    # lower case letters
    dic['z'] = 'a'
    for i in range(ord('a'), ord('z')):
        dic[chr(i)] = chr(i + 1)
    # upper case letters
    dic['Z'] = 'A'
    for i in range(ord('A'), ord('Z')):
        dic[chr(i)] = chr(i + 1)
    # space, stop and some other special characters
    dic[' '] = '$'
    dic['.'] = '#'
    dic['#'] = '.'
    dic['$'] = ' '
    dic['?'] = '!'
    dic['!'] = '?'
    return dic


def check_code_is_reversible(dic):
    """Given a dictionary used as a code mapping, this function checks
    whether the set of keys is the same set of values: if the elements
    in the keys are the same unique set as those in the values, then
    this mapping is bijective (the set of values is then actually a
    permutation of the set of input values) and can be inverted.

    If this is not the case, some debug information is printed, and a
    ValueError exception raised.
    """

    unique_keys = set()
    unique_vals = set()
    for key, val in dic.items():
        unique_keys.add(key)
        unique_vals.add(val)
    if unique_vals != unique_keys:
        print "Code is not reversible:"
        print "keys are   %s", sorted(unique_keys)
        print "values are %s", sorted(unique_vals)
        raise ValueError("Code is not reversible - stopping here")
    return True


def test_codes():
    """Check that codes defined above are reversible."""
    for c in (code0(), code1(), code2(), code3()):
        assert check_code_is_reversible(c)


secretmessage = \
    "Zpv$ibwf$tvddfttgvmmz$efdpefe$uijt$tfdsfu$nfttbhf#$Dpohsbuvmbujpot?"


# if this file is executed on it's own, check codes given
if __name__ == "__main__":
    test_codes()


def trapezoidal(f, a, b, n):
    """Takes a function f(), upper limit b, lower limit a,
    and number of subdivisions n and approximates an integral using the
    trapezoidal rule"""
    a = float(a)   # Avoiding floating point issues
    b = float(b)
    h = (b - a)/n   # Setting up h
    xs = []   # Creating empty list
    for i in range(n):
        xs.append(a + i * h)
    sum = 0
    for j in xs:   # Creation of sigma term
        sum += f(j)
    trap_ends = f(a) + f(b)   # Creation of ends
    A = (h / 2.0) * (trap_ends + 2 * sum)
    return A


def trapez(f, a, b, n):
    """Approximates and returns the definite integral of f from a to b by
    the composite trapezoidal rule, using n subintervals"""
    aprime = float(a)
    bprime = float(b)
    nprime = float(n)
    h = (bprime - aprime) / nprime
    s = f(aprime) + f(bprime)
    for i in xrange(1, n):
        s += 2 * f(aprime + i * h)
    return s * h / 2.0


def encode(code, msg):
    """Encodesand returns a message by interchanging certain letters in a
    message msg for those defined by the key dictionary inputted in code"""
    new = ''.join(code.get(ch, ch) for ch in msg)
    return new


def reverse_dic(d):
    """Computes and returns the reverse of a dictionary d: ie, the key k and
    value v becomes the key v and value k"""
    res = dict((v, k) for k, v in iteritems(d))
    return res


def decode(code, encoded_msg):
    """Decodes a message by interchanging certain letters in an
    encrypted message msg for those defined by the key dictionary inputted in
    code after reversing using reverse_dic() and returns the result"""
    code_prime = reverse_dic(code)
    return encode(code_prime, encoded_msg)
