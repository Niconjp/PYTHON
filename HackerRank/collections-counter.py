# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

tShoes = int(input())
shoes = Counter([int(x) for x in input().split()])
customer = int(input())
count1 = 0
tMoney = 0

while count1 < customer:
    Shoes,Prices = map(int,input().split())
    
    if shoes[Shoes]:
        tMoney += Prices
        shoes[Shoes] -= 1
        
    count1 += 1
    
print(tMoney)
