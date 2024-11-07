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
MOD = 10**9+7

# DFS
def dfs(v, pv):
    dp[v][2] = 1
    if C[v] == 'a':
        dp[v][0] = 1
    else:
        dp[v][1] = 1
    
    for nv in G[v]:
        if nv == pv:
            continue
        dfs(nv, v)

        # もしv='a'なら、そこから延びる枝はa,b両方を持っているか、aしか含まない
        # 枝がaのみ枝になる
        dp[v][0] *= dp[nv][0] + dp[nv][2]
        dp[v][0] %= MOD
        # もしv='b'なら、そこから延びる枝はa,b両方を持っているか、bしか含まない
        # 枝がbのみ枝になる
        dp[v][1] *= dp[nv][1] + dp[nv][2]
        dp[v][1] %= MOD
        # 
        # 
        dp[v][2] *= sum(dp[nv]) + dp[nv][2]
        dp[v][2] %= MOD

    dp[v][2] -= dp[v][0] + dp[v][1]
    dp[v][2] %= MOD

#main
def main():
    # intput
    N = int(input())
    global C
    C = list(input().split(' ')) 
    global G
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split(' '))
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    # dp[pos][状態] := 可能な数
    global dp
    dp = [[0]*3 for _ in range(N)]

    dfs(0, -1)
    print(dp[0][2])

if __name__ == '__main__':
    main()