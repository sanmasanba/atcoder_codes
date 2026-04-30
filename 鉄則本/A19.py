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
    N, W = map(int, input().split())
    w, v = zip(*[list(map(int, input().split())) for _ in range(N)])

    dp = [[-1]*(W+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        ww, vv = w[i], v[i]
        for j in range(W+1):
            dp[i+1][j] = max(dp[i][j], dp[i+1][j])
            if 0 <= j-ww and 0 <= dp[i][j-ww]:
                dp[i+1][j] = max(dp[i][j-ww]+vv, dp[i+1][j])

    print(max(dp[-1]))

if __name__ == '__main__':
    main()