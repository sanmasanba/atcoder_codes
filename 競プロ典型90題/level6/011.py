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
    N = int(input())
    DCS = []
    max_d = 0
    for _ in range(N):
        tmp = list(map(int, input().split()))
        max_d = max(max_d, tmp[0])
        DCS.append(tmp)
    DCS.sort()

    # DP
    dp = [[0] * (max_d+1) for _ in range(N+1)]

    for i in range(N):
        d, c, s = DCS[i]
        for j in range(1, max_d+1):
            if j <= d and 1 <= j - c + 1:
                dp[i+1][j] = max(dp[i][j], dp[i][j-c] + s)
            else:
                dp[i+1][j] = max(dp[i][j], dp[i+1][j-1])

    print(dp[N][max_d])

if __name__ == '__main__':
    main()