# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/python

# 4 kyu

# Snail

def snail(array):
    arr = []
    while len(array) > 0:
        arr += array[0]
        del array[0]
        if len(array) > 0:
            for i in array:
                arr += [i[-1]]
                del i[-1]
            if array[-1]:
                arr += array[-1][::-1]
                del array[-1]
            for i in reversed(array):
                arr += [i[0]]
                del i[0]
    return arr

# OR
import numpy as np

def snail(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m


