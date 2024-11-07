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
def dfs(pre, pos, G, dp):
    # 通過したら記録
    dp[pos] += 1
    for nxt in G[pos]:
        if pre != nxt:
            dfs(pos, nxt, G, dp)
            # 下のノードの個数を数える
            dp[pos] += dp[nxt]

#main
def main():
    # intput
    N = int(input())
    G = [[] for _ in range(N)]
    edges = []
    for _ in range(N-1):
        a, b = map(lambda x: int(x)-1, input().split(' '))
        G[a].append(b)
        G[b].append(a)
        edges.append([a, b])

    dp = [0] * N
    # ノードの通過回数を求める
    dfs(-1, 0, G, dp)

    res = 0
    for a, b in edges:
        r = min(dp[a], dp[b])
        res += r * (N-r)
    
    print(dp)
    print(res)

if __name__ == '__main__':
    main()