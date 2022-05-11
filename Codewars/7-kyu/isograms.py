# https://www.codewars.com/kata/54ba84be607a92aa900000f1/python

# 7 kyu

# Isograms

def is_isogram(string):
    dup = []
    string= string.lower()
    for c in string:
        if string.count(c) > 1:
            if c not in dup:
                dup.append(c)
    if not dup:
        return True
    else:
        return False

def is_isogram(string):
    string = string.lower()
    a = set(string)
    if len(string) == len(a):
        return True
    else:
        return False

def is_isogram(string):
    return len(string) == len(set(string.lower()))
