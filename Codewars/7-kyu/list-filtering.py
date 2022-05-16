# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/python

# 7 kyu

# List Filtering

def filter_list(l):
    nLst = []
    for x in l:
        if type(x) != str:
            nLst.append(x)
    return nLst

# 'return a new list with the strings filtered out'
