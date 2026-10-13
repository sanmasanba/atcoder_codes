# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, isqrt, pi, gcd, lcm, factorial
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
    P = [[] for _ in range(N)]
    for i, p in enumerate(map(lambda x: int(x)-1, input().split()), start=1):
        P[i].append(p)
        P[p].append(i)

    # DFS
    tin, tout = [0]*N, [-1]*N
    depth = defaultdict(list)
    seen = set()
    def dfs(v, d=0):
        # 頂点vを探索済みにする
        tin[v] = len(seen)
        # 深さごとに記録
        depth[d].append(len(seen))
        seen.add(v)
        # 探索
        for next_v in P[v]:
            if next_v in seen:
                continue
            dfs(next_v, d+1)
            
        tout[v] = len(seen)
        return tin[v]
    dfs(0)

    Q = int(input())
    for _ in range(Q):
        U, D = map(int, input().split())
        U -= 1
        # depth にない場合はその深さのノードがない
        if (d := depth.get(D)) is None:
            print(0)
            continue
        a, b = tin[U], tout[U]
        print(bisect_left(d, b) - bisect_left(d, a))

if __name__ == '__main__':
    main()
