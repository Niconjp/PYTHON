# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

a,b =input().split()
b = int(b)

c = sorted(list(permutations(a,b)))

for x in c:
    print(''.join(x))
