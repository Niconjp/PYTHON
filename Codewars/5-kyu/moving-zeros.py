# https://www.codewars.com/kata/52597aa56021e91c93000cb0/python

# 5 kyu

# Moving Zeros To The End

def move_zeros(array):
    a = []
    i = 0
    for x in array:
        if x != 0:
            a.append(x)
        else:
            i += 1
    for x in range(i):
        a.append(0)
    
    return a
    
 # OR
 
 def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)
