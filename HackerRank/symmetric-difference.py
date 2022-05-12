# https://www.hackerrank.com/challenges/symmetric-difference/problem

n = int(input())
arr = set(list(map(int,input().split())))
n1 = int(input())
arr2 = set(list(map(int,input().split())))

a = sorted(arr.difference(arr2).union(arr2.difference(arr)))

for x in range(len(a)):
    print(a[x])
