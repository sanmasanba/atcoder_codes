#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

import time

sys.setrecursionlimit(500000)
INF = float('inf')

@lru_cache
def chr(N, X, Y):
    if N == 1:
        return 0
    else:
        return chr(N-1, X, Y) + X*chb(N, X, Y)

@lru_cache
def chb(N, X, Y):
    if N == 1:
        return 1
    else:
        return chr(N-1, X, Y) + Y*chb(N-1, X, Y)

#main
def main():
    N, X, Y = map(int, input().split(' '))
    
    start = time.time_ns()
    res = chr(N, X, Y)
    end = time.time_ns()
    print(res, end-start)

if __name__ == '__main__':
    main()