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

#main
def main():
    # intput
    N, Q = map(int, input().split(' '))
    X = list(map(int, input().split(' ')))
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(lambda x: int(x)-1, input().split(' '))
        G[a].append(b)
        G[b].append(a)
    node = [[] for _ in range(N)]

    # DFS
    def dfs(v, p=-1):
        for next_v in G[v]:
            if next_v == p:
                continue
            node[v].extend(dfs(next_v, v))
            node[v].sort()
            if 20 < len(node[v]):
                node[v] = node[v][-20:]

        node[v].append(X[v])
        node[v].sort()
        return node[v]

    dfs(0)

    for _ in range(Q):
        V, K = map(int, input().split(' '))
        print(node[V-1][-K])

if __name__ == '__main__':
    main()