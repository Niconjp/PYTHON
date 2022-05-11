# https://www.codewars.com/kata/5390bac347d09b7da40006f6/python

# 7 kyu

# Jaden Casing Strings

def toJadenCase(s):
  " ".join(w.capitalize() for w in s.split())
