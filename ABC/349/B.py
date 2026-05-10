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
    C = dict()

    for s in S:
        if s not in C:
            C[s] = 0
        C[s] += 1
    cnt = Counter(C.values())
    res = 'Yes'
    for v in cnt.values():
        if v != 2:
            res = 'No'
    print(res)

if __name__ == '__main__':
    main()