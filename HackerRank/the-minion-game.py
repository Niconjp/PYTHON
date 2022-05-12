# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    a = 0
    b = 0
    for i, c in enumerate(s):
        if c in vowels:
            b += len(string) - i
        else:
            a += len(string) - i

    if a == b:
        print ("Draw")
    elif a > b:
        print ('Stuart {}'.format(a))
    else:
        print ('Kevin {}'.format(b))
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
