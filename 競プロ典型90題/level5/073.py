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

#main
def main():
    # intput
    N = int(input())
    C = list(input().split(' ')) 
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split(' '))
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    # dp[pos][状態] := 可能な数(0: aのみ,1: bのみ,2: aとb)
    dp = [[0]*3 for _ in range(N)]

    # DFS
    def dfs(v, pv=-1):
        either, both = 1, 1
        if C[v] == 'a': 
            c = 0  
        else: 
            c = 1
        
        for nv in G[v]:
            if nv == pv:
                continue
            dfs(nv, v)
            # either := 自身と同じ文字しかない部分木 + abの両方を含む部分木
            # both := aのみの部分木 + bのみの部分木 + abを含む部分木(つないでもつながなくても)
            either *= (dp[nv][c] + dp[nv][2])
            both *= (dp[nv][0] + dp[nv][1] + 2*dp[nv][2])
            either %= MOD
            both %= MOD

        dp[v][c] = either
        dp[v][2] = (both - either + MOD) % MOD

    dfs(0)
    print(dp[0][2])

if __name__ == '__main__':
    main()