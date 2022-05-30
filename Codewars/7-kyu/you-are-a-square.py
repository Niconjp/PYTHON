# https://www.codewars.com/kata/54c27a33fb7da0db0100040e

# 7 Kyu

# You're a square!

def is_square(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    else:
        p = int(n ** 0.5)
        if p * p == n:
            return True
        else:
            return False

# OR

from math import sqrt

def is_square(n):    
    return n>=0 and sqrt(n).is_integer()
