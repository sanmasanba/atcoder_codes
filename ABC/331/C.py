#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

def func(a, A, A_cumulative):
    pos = bisect_right(A, a)
    return A_cumulative[-1] - A_cumulative[pos]

#main
def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    sort_A = sorted(A)

    A_ele = set(A)
    A_cumulative = [0 for _ in range(N+1)]
    for i, a in enumerate(sort_A):
        A_cumulative[i+1] = (A_cumulative[i]+a)
    A_set = {a:func(a, sort_A, A_cumulative) for a in A_ele}

    for a in A:
        print(A_set[a], end=' ')

if __name__ == '__main__':
    main()