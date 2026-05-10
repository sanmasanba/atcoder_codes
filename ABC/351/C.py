#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    
    num = 0
    res = deque()
    for i in range(N):
        res.append(A[i])
        num += 1
        if i == 0:
            #print(i+1, res)
            continue
        else:
            while 1:
                if num == 1 or res[-2] != res[-1]:
                    break
                else:
                    num -= 1
                    tmp = res.pop()
                    res.pop()
                    res.append(tmp+1)

        #print(i+1, res)

    print(len(res))





if __name__ == '__main__':
    main()