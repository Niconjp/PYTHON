# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem


import re

s = input()

l1 = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([aeiouAEIOU]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])',s)

if l1 == []:
    print("-1")
else:
    for _ in range(len(l1)):
        print(l1[_])
