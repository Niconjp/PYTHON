# https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    newstring = ''
    for x in s:
        if x.isupper() == True:
            newstring+=(x.lower())
        elif x.islower() == True:
            newstring+=(x.upper())
        elif x.isalpha()== False:
            newstring+= (x)
    return newstring
            
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
