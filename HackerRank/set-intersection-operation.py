# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

a = input()
b = input().split()
c = input()
d = input().split()

s1 = set(b)

s2 = s1.intersection(d)

s3 = len(s2)

print(s3)
