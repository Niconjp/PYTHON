# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    st = set(array)
    avg = sum(st) / len(st)
    return avg
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
