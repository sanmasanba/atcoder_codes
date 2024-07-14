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
    N, L, R = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    res = []
    for a in A:
        if a <= L:
            res.append(L)
        elif L < a < R:
            res.append(a)
        else:
            res.append(R)
    print(*res)

if __name__ == '__main__':
    main()