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
    N, M = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    
    sigma = [0]
    for i in A:
        sigma.append(i+sigma[-1])

    tmp = 0
    for i in range(M):
        tmp += (i+1)*A[i]
    res = tmp
    for i in range(1, N-M+1):
        tmp = tmp + (M*A[i+M-1] - (sigma[i+M-1] - sigma[i-1]))
        res = max(tmp, res)
    
    print(res)

if __name__ == '__main__':
    main()