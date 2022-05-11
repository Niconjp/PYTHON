# https://www.codewars.com/kata/5208f99aee097e6552000148/python

# 6 kyu

# Break camelCase

import re
def solution(s):
    a = []
    a = re.findall('[a-zA-Z][^A-Z]*', s)
    return " ".join(str(x) for x in a)
  
# OR

def solution(s):
  return ''.join(' ' + c if c.isupper() else c for c in s)
