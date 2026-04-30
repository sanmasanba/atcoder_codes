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
    G = [[] for _ in range(N+1)]
    G[0].append(1)
    G[1].append(0)
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    
    # dp[i][j] := 頂点i以下の部分木で可能な塗り方の数
    # j = 0: white, 1: black
    dp = [[1]*2 for _ in range(N+1)]
    seen = set()
    def dfs(v=0):
        seen.add(v)
        for next_v in G[v]:
            if next_v in seen:
                continue
            dfs(next_v)
            # dp[v][0] : 連続する部分木の根の色は問わない
            dp[v][0] = (dp[v][0] * sum(dp[next_v])) % MOD1e7
            # dp[v][1] : 連続する部分木の根は白のみ許される
            dp[v][1] = (dp[v][1] * dp[next_v][0]) % MOD1e7
        seen.remove(v)
    dfs()
    
    print(dp[0][0])

if __name__ == '__main__':
    main()