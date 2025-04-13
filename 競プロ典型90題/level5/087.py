#library
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
MOD998244353 = 998244353
MOD1000000007 = 1000000007

#main
def main():
    # intput
    N, P, K = map(int, input().split())
    G = [list(map(int, input().split())) for _ in range(N)]

    dp = [[INF if G[i][j] == -1 else G[i][j] for j in range(N)] for i in range(N)]
    # step1 X = P+1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if dp[i][j] <= P:
                cnt += 1
    if cnt == K:
        print('Infinity')
        return
    
    def counter(m):
        dp = [[m if G[i][j] == -1 else G[i][j] for j in range(N)] for i in range(N)]
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])        
        cnt = 0
        for i in range(N):
            for j in range(i+1, N):
                if dp[i][j] <= P:
                    cnt += 1        
        return cnt

    def solve(cnt):
        cl, cr, minx = 1, 1 << 30, 1 << 30
        for _ in range(41):
            mid = (cr + cl) // 2
            res = counter(mid)
            if res <= cnt:
                cr, minx = mid, min(minx, mid)
            else:
                cl = mid
        return minx

    # f(x) <= Kが成り立つXの最小値L
    L = solve(K)
    # f(x) < Kが成り立つXの最小値R
    R = solve(K-1)
    print(R-L)

if __name__ == '__main__':
    main()