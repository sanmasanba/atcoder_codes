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
    A = list(map(int, input().split()))
    
    G = defaultdict(set)
    for i, a in enumerate(A, start=1):
        G[a].add(2*i)
        G[a].add(2*i+1)
    
    def bfs():
        # dist:vからの距離, queue:探索キュー
        dist = [-1 for _ in range(2*N+2)]
        queue = deque()
        dist[1] = 0
        queue.append(1)
        while queue:
            v = queue.popleft()
            for next_v in G[v]:
                if dist[next_v] != -1:
                    continue
                dist[next_v] = dist[v] + 1
                queue.append(next_v)
        return dist
    res = bfs()

    for r in res[1:]:
        if r == -1:
            break
        print(r)

if __name__ == '__main__':
    main()