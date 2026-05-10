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
    A = list(map(int, input().split(' ')))
    A.sort()

    res = INF
    #print(*A)
    for i in range(K+1):
        tmp = A[-K + i - 1] - A[i]
        #print(A[-K + i - 1], A[i])
        res = min(tmp, res) 

    if N - K == 1:
        print(0)
    else:
        print(res)

if __name__ == '__main__':
    main()