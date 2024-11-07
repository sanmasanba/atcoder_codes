#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop, heapify
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

res = []
def dfs(v):
    res.append(v+1)
    global seen
    seen[v] = True
    while G[v]:
        next_v = heappop(G[v])
        if seen[next_v]:
            continue
        dfs(next_v)
        res.append(v+1)

#main
def main():
    # intput
    N = int(input())
    global G
    global seen
    seen = [False] * N
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(lambda x: int(x)-1, input().split(' '))
        heappush(G[a], b)
        heappush(G[b], a)

    dfs(0)
    print(*res)

if __name__ == '__main__':
    main()