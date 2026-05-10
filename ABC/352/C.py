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
    A, B = [], []
    S = 0
    for _ in range(N):
        a, b = map(int, input().split(' '))
        A.append(a)
        B.append(b)
        S += a

    res = S - A[0] + B[0]
    for i in range(1, N):
        tmp = S - A[i] + B[i]
        res = max(res, tmp)
    print(res)

if __name__ == '__main__':
    main()