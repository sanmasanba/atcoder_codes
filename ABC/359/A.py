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
    L = [input() for _ in range(N)]
    
    res = 0
    for i in L:
        if i == 'Takahashi':
            res += 1

    print(res)

if __name__ == '__main__':
    main()