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
    S = list(input())

    r = S.index('R')
    m = S.index('M')

    res = 'Yes' if r < m else 'No'
    print(res)

if __name__ == '__main__':
    main()