# https://www.hackerrank.com/challenges/designer-door-mat/problem

N,M = input().split()
N = int(N)
M = int(M)

string = 'WELCOME'
g = '-'
a = '.|.'

for i in range(1,N,2): 
    print((i * a).center(M, g))
print(string.center(M,g))
for i in range(N-2,-1,-2): 
    print((i * a).center(M, g))
