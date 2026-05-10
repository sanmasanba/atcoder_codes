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
    N, M = map(int, input().split())
    G = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        G[a].add(b)

    reachable = [[] for _ in range(N)]
    
    def bfs(s):
        dist = [False for _ in range(N+1)]
        queue = deque()
        dist[s] = True
        queue.append(s)
        while queue:
            v = queue.popleft()
            for next_v in G[v]:
                if dist[next_v]:
                    continue
                dist[next_v] = True
                queue.append(next_v)
        return [i for i, b in enumerate(dist) if b]
    
    for a in range(N):
        reachable[a] = bfs(a)

    res = 0
    for a in range(N):
        for c in reachable[a]:
            if c not in G[a] and a != c:
                res += 1
                G[a].add(c)
    print(res)

if __name__ == '__main__':
    main()