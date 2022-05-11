# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/python

# 5 kyu

# String incrementer

import re
def increment_string(string):
    lst = re.split('(\d+)',string)
    del lst[-1]
    if string.isalpha() == True:
        string += '1'
        return string
    elif string == '':
        string += '1'
        return string
    elif len(lst) >= 2:
        a = lst[-1]
        if a.isnumeric() == True:
            b = int(a) + 1
            c = str(b).zfill(len(a))
            del lst[-1]
            lst.append(c)
    return ''.join(map(str,lst))
  
  # OR
  
  def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))
