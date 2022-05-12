# https://www.hackerrank.com/challenges/the-minion-game/problem

import itertools

def minion_game(string):
    points = 0 #Stuart
    pointsK = 0 #Keving
    for x in string:
        if x != "A" and "E" and "I" and "O" and "U":
           points += 1
    return print(f"{points}")   
        
def permutations(string):
    permutations = []
    for l in range(1,len(string)+1):
        for p in itertools.permutations(string,l):
            permutations.append("".join(permutations))
    return permutations
    
if __name__ == '__main__':
    s = "BANANA"
    #minion_game(s)
    permutations(s)
