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
    A = list(map(lambda x: int(x)-1, input().split(' ')))
    
    res = []
    K = 0
    for i in range(N):
        while A[i] != i:
            K += 1
            res.append((i+1, A[i]+1)) 
            tmp = A[A[i]]
            A[A[i]] = A[i]
            A[i] = tmp

    print(K)
    [print(*i) for i in res]

if __name__ == '__main__':
    main()