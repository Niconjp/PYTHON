# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/python

# Strip Comments

# 4 kyu

def strip_comments(strng, markers):
  nStrng = strng.splitlines()
  for i in markers:
    nStrng = [s.split(i)[0].rstrip() for s in nStrng]
  return '\n'.join(nStrng)
