# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/python

# 5 kyu

# Maximum subarray sum

# Kadane's Algorithm

def max_sequence(arr):
    size = len(arr)
    if size == 0:
        return 0
    elif size == 1:
        return arr[0]
    if size > 2:
        a = []
        for x in arr:
            if x < 0:
                a.append(x)
        if len(a) == size:
            return 0
        else:
            max_so_far =arr[0]
            curr_max = arr[0]
            for i in range(1,size):
                curr_max = max(arr[i], curr_max + arr[i])
                max_so_far = max(max_so_far,curr_max)
            return max_so_far

# OR

def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max
