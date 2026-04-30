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
    N = int(input())
    P, A = [0]*2001, [0]*2001
    for i in range(1, N+1):
        p, a = map(int, input().split())
        P[i], A[i] = p, a
        
    dp = [[0]*(2001) for _ in range(2001)]
    dp[1][N] = 0
    for len in range(N-2, -1, -1):
        for l in range(1, N-len+1):
            r = l + len

            if l == 1:
                dp[l][r] = dp[l][r+1] + (A[r+1] if l <= P[r+1] <= r else 0)
            elif r == N:
                dp[l][r] = dp[l-1][r] + (A[l-1] if l <= P[l-1] <= r else 0)
            else:
                dp[l][r] = max(dp[l][r+1] + (A[r+1] if l <= P[r+1] <= r else 0),
                               dp[l-1][r] + (A[l-1] if l <= P[l-1] <= r else 0))

    res = 0
    for i in range(1, N+1):
        res = max(res, dp[i][i])
    print(res)

if __name__ == '__main__':
    main()