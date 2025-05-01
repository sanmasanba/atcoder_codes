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
    N, X = map(int, input().split())
    SCP = []
    for _ in range(N):
        s, c, p = map(int, input().split())
        p /= 100
        SCP.append([s, c, p])

    # dp[i][j] := すでにiで現れる問題に正解していて、残金がj円であるときの最大期待値
    dp = [[0]*(X+1) for _ in range(2**N)]
    for x in range(X+1):
        for state in range(2**N):
            for i in range(N):
                s, c, p = SCP[i]
                if x-c < 0:
                    continue
                if not (state >> i & 1):
                    # exp := 未正解の問題に対して、c円払って
                    # (1) 確率pで正解        -> x-c円で、state+(1<<i)の状態
                    # (2) 確率(1-p)で不正解  -> x-c円で、stateの状態
                    # となるので、dp[state][x] := p*(1) + (1-p)*(2)
                    exp = p*(dp[state+(1<<i)][x-c] + s) + (1-p)*dp[state][x-c]
                    dp[state][x] = max(dp[state][x], exp)
    print(dp[0][X])

if __name__ == '__main__':
    main()