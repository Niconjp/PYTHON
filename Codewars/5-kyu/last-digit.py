# https://www.codewars.com/kata/5511b2f550906349a70004e1/python

# 5 Kyu

# Last digit of a large number


def last_digit(n1, n2):
    if n2 == 0:
        return 1
    elif n2 == 1:
        return n1
    else:
        a = pow(n1,n2,10) 
        return a

# OR

def last_digit(n1, n2):
    return pow( n1, n2, 10 )
