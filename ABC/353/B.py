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
    N, K = map(int, input().split(' '))
    A = deque(map(int, input().split(' ')))
    
    res = 0
    chair = K
    while 1:
        if len(A) == 0:
            res += 1
            #print(res)
            break
        else:
            a = A[0]
            if chair < a:
                res += 1
                chair = K
                #print(res)
            else:
                a = A.popleft()
                chair -= a
                #print(chair)

    print(res)

if __name__ == '__main__':
    main()