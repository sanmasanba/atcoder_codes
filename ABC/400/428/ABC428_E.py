# library
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

# main
def main():
    # intput
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(lambda x: int(x)-1, input().split())
        G[a].append(b)
        G[b].append(a)
    
    # BFS
    def bfs(s):
        # dist:vからの距離, queue:探索キュー
        dist = [-1 for _ in range(N)]
        queue = deque()
        dist[s] = 0
        queue.append(s)
        while queue:
            v = queue.popleft()
            for next_v in G[v]:
                if dist[next_v] != -1:
                    continue
                dist[next_v] = dist[v] + 1
                queue.append(next_v)
        return v
    v = bfs(0)
    v = bfs(v)
    
    # DFS
    seen = set()
    dist = [[-1, -1] for _ in range(N)]
    def dfs(v, s, sd):
        seen.add(v)
        c, cd = dist[v]
        if cd == sd:
            dist[v] = [max(c, s), cd]
        elif cd < sd:
             dist[v] = [s, sd]
        for nv in G[v]:
            if nv in seen:
                continue
            c, cd = dist[v]
            t, td = dfs(nv, c, cd)
            if cd == td:
                dist[v] = [max(c, t), td]
            elif cd < td:
                dist[v] = [t, td]
        seen.remove(v)
        return dist[v][0], dist[v][1]

    dfs(v, -1, -1)
    for d, _ in dist: print(d)

if __name__ == '__main__':
    main()