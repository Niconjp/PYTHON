# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    lst= []
    scoreLst = []
    ScoreMin = 0
    NamesMin = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name,score])
        scoreLst.append(score)
    
    scoreLst = list(set(scoreLst))
    scoreLst.sort()
    ScoreMin = scoreLst[1]
    
    for x in range(len(lst)):
        if lst[x][1] == ScoreMin:
            NamesMin.append(lst[x][0])
            
    NamesMin.sort()
            
    print(*NamesMin, sep="\n")
