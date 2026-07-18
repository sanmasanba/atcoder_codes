# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, NamedTuple, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

def solve():
    N = int(input())
    S = list(input().strip())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    
    dp = [[0]*2 for _ in range(N)]
    if S[0] == 'S':
        dp[0][0] = 0
        dp[0][1] = -X[0]
    else:
        dp[0][0] = -X[0]
        dp[0][1] = 0

    for i in range(N-1):
        f = S[i+1]
        # もし、iがSならば
        dp[i+1][0] = max(
            dp[i][0] + (-X[i+1] if f == 'R' else 0)   # S -> S
            , dp[i][1] + (-X[i+1] if f == 'R' else 0) + Y[i]  # R -> S
        )
        dp[i+1][1] = max(
            dp[i][0] + (-X[i+1] if f == 'S' else 0)   # S -> R
            , dp[i][1] + (-X[i+1] if f == 'S' else 0) # R -> R
        )
    print(max(dp[-1]))

# main
def main():
    # intput
    T = int(input())
    for t in range(T):
        solve()

if __name__ == '__main__':
    main()