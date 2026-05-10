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
    P = list(map(int, input().split(' ')))
    Q = int(input())
    A, B = [], []
    for _ in range(Q):
        a, b = map(int, input().split(' '))
        A.append(a)
        B.append(b)
    for i in range(Q):
        print(A[i] if P.index(A[i]) < P.index(B[i]) else B[i])

if __name__ == '__main__':
    main()