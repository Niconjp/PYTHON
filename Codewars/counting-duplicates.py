# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/python

# 6 kyu

# Counting Duplicates

def duplicate_count(text):
    text = text.lower()
    lst = []
    for i in text:
        if text.count(i) > 1:
            lst.append(i)
    dC= len(set(lst))
    return dC

def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c)>1])
