# https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product

a = list(input().split()) # [int(x) for x in input().split()]
num1 = [int(i) for i in a] # 
b = list(input().split())
num2 = [int(i) for i in b]
c=list(product(num1,num2))
print(*c)

