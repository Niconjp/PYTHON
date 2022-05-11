# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/python

# 6 kyu

# Find the unique number

def find_uniq(arr):
    a = set(arr)
    for x in a:
        if arr.count(x) == 1:
            return x
