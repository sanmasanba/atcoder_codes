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

# main
def main():
    # intput
    N = int(input())
    cost = [[0]*N for _ in range(N)]
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())

    for i in range(N-1):
        A = list(map(int, input().split()))
        for j, a in enumerate(A):
            cost[i][j+1+i] = a
            cost[j+1+i][i] = a

    seen = set()
    def _dfs(G, v):
        # 頂点vを探索済みにする
        seen.add(v)

        # 探索
        for next_v in G[v]:
            # 探索済みならスルー
            if next_v in seen:
                continue
            return _dfs(G, next_v)
        return v
    v = _dfs(0)
    root = _dfs(v)
    print(root)

if __name__ == '__main__':
    main()