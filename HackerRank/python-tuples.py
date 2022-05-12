# https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(raw_input())
    
    integer_list = map(int, raw_input().split())
    tuplelst = tuple(integer_list)
    tuplehast = hash(tuplelst)
    
    print(tuplehast) 
