from math import pow, sqrt

def calc_pythagoras(a, b):
    """
    Function that applies Pythagoras

    Input: 
    * a: a side of the triangle
    * b: b side of the triangle
    """
    c_sqrd = pow(a, 2) + pow(b, 2)
    c = sqrt(c_sqrd)
    return c