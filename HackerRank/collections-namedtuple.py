# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

N = int(input())
F = list(input().split())

students = namedtuple('student',F)

sumT = 0
for x in range(N):
    f1,f2,f3,f4 = input().split()
    student = students(f1,f2,f3,f4)
    sumT += int(student.MARKS)
    
print(sumT/N)
