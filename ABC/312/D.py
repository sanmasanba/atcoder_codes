#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')
MOD = 998244353

#main
def main():
    # intput
    S = list(input())
    N = len(S)

    # dp[i][j] := i文字目まで見て、'(' = 1、')' = -1と見た時の総和がjとなる組の数
    dp = [[0]*3010 for _ in range(3010)]
    dp[0][0] = 1
    for i, s in enumerate(S):
        match s:
            case '(':
                for j in range(1, 3001):
                    dp[i+1][j] = dp[i][j-1]
                    dp[i+1][j] %= MOD
            case ')':
                for j in range(3001):
                    dp[i+1][j] = dp[i][j+1]
                    dp[i+1][j] %= MOD
            case '?':
                for j in range(3001):
                    dp[i+1][j] += dp[i][j+1]
                    if 0 < j:
                        dp[i+1][j] += dp[i][j-1]
                    dp[i+1][j] %= MOD
    
    print(dp[N][0]%MOD)

if __name__ == '__main__':
    main()