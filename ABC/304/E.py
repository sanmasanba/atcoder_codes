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
    N, M = map(int, input().split())
    G = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].add(b-1)
        G[b-1].add(a-1)
    
    union = [-1]*N
    #BFS
    def bfs(s):
        queue = deque()
        union[s] = s
        queue.append(s)
        while queue:
            v = queue.popleft()
            for next_v in G[v]:
                if union[next_v] != -1:
                    continue
                union[next_v] = union[v]
                queue.append(next_v)

    for s in range(N):
        if union[s] == -1:
            bfs(s)

    K = int(input())
    xy = set()
    for _ in range(K):
        x, y = map(lambda x: int(x)-1, input().split())
        x, y = union[x], union[y]
        if x > y:
            x, y = y, x
        xy.add((x, y))
    
    Q = int(input())
    for _ in range(Q):
        p, q = map(lambda x: int(x)-1, input().split())
        p, q = union[p], union[q]
        if p > q:
            p, q = q, p
        if p == q:
            print('Yes')
        elif (p, q) in xy:
            print('No')
        else:
            print('Yes')

if __name__ == '__main__':
    main()