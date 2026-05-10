# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

_dhs = [[-1, -1, 0], [-1, -1, 0], [0, 1, 1], [0, 1, 1]]
_dws = [[-1, 0, -1], [0, 1, 1], [-1, -1, 0], [1, 0, 1]]

def solve():
    H, W = map(int, input().split())
    M = [list(input().strip()) for _ in range(H)]
    memo = [[0]*W for _ in range(H)] 

    def check(h, w, dhs, dws):
        for dh, dw in zip(dhs, dws):
            nh, nw = h+dh, w+dw
            if not (0 <= nh < H) or not (0 <= nw < W): return
            if M[nh][nw] == '.': return
        memo[h][w] += 1

    for h in range(H):
        for w in range(W):
            if M[h][w] == '#':
                for dhs, dws in zip(_dhs, _dws):
                    check(h, w, dhs, dws)
    q = []
    for i, m in enumerate(memo):
        for j, c in enumerate(m):
            if 0 < c:
                heappush(q, (-c, i, j))
    res = 0
    while q:
        c, h, w = heappop(q)
        if memo[h][w] != -c: 
            continue
        res += 1
        M[h][w] = '.'
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not (0 <= h+i < H) or not (0 <= w+j < W): 
                    continue
                memo[h+i][w+j] = 0
                if M[h+i][w+j] == '#':
                    for dhs, dws in zip(_dhs, _dws):
                        check(h+i, w+j, dhs, dws)
                if 0 < memo[h+i][w+j]: 
                    heappush(q, (-memo[h+i][w+j], h+i, w+j))
    print(res)

# main
def main():
    # intput
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()