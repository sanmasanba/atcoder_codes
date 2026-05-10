#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, M = map(int, input().split(' '))
    S = list(input())
    T = list(input())

    pre = 0
    suf = 0
    for n in range(N):
        if T[n] != S[n]:
            pre = 1
    for n in range(N):
        if T[n+M-N] != S[n]:
            suf = 1
    
    print((int(f"{pre}{suf}", 2)))

if __name__ == '__main__':
    main()