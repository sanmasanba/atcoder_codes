#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

@lru_cache
def func(N):
    if N == 1:
        return 0
    tmp_ceil = (N+1)//2
    tmp_floor = N//2
    return N + func(tmp_ceil) + func(tmp_floor)

#main
def main():
    N = int(input())   
    print(func(N))

if __name__ == '__main__':
    main()