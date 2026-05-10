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
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
        
    #BFS
    dist = [-1 for _ in range(N+1)]
    def bfs(x, k):
        if k == 0:
            return x
        reached = []
        reached.append(x)
        queue = deque()
        queue.append(x)
        dist[x] = 0
        while queue:
            v = queue.popleft()
            for next_v in G[v]:
                if dist[next_v] != -1:
                    continue
                dist[next_v] = dist[v]+1
                reached.append(next_v)
                if dist[next_v] < k:
                    queue.append(next_v)
        for r in reached: dist[r] = -1
        return sum(reached)

    res = []
    Q = int(input())
    for _ in range(Q):
        x, k = map(int, input().split())
        res.append(bfs(x, k))
    print(*res, sep='\n')

if __name__ == '__main__':
    main()