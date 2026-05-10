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
    N = len(S)
    res = set()
    for i in range(N):
        for j in range(i, N+1):
            res.add(tuple(S[i:j]))

    print(len(res)-1)
if __name__ == '__main__':
    main()