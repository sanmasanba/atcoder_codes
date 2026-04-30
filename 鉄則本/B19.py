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
MOD998 = 998244353
MOD1e7 = 1000000007

#main
def main():
    # intput
    N, WW = map(int, input().split())
    W, V = [0]*N, [0]*N
    for i in range(N):
        w, v = map(int, input().split())
        W[i], V[i] = w, v

    dp = [[INF]*(100001) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        w, v = W[i], V[i]
        for j in range(100001):
            if dp[i][j] != INF:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j])
                if j+v <= 100000:
                    dp[i+1][j+v] = min(dp[i+1][j+v], dp[i][j] + w)
    
    res = 0
    for v, w in enumerate(dp[N]):
        if w <= WW:
            res = v
    print(res)

if __name__ == '__main__':
    main()