#library
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

def solver():
    N, K = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(lambda x: int(x)-1, input().split())
        G[a].append(b)
        G[b].append(a)
    
    new_G = [set() for _ in range(N)]
    #BFS
    def bfs1(s):
        dist = [-1 for _ in range(N+1)]
        queue = deque()
        dist[s] = 0
        queue.append(s)
        while queue:
            v = queue.popleft()
            for next_v in G[v]:
                if dist[next_v] != -1:
                    continue
                dist[next_v] = dist[v] + 1
                if dist[next_v] == K:
                    new_G[s].add(next_v)
                    continue
                queue.append(next_v)

    #BFS
    def bfs(G, N, s):
        dist = [-1 for _ in range(N+1)]
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
        return dist

    for s in range(N):
        bfs1(s)
    res = bfs(new_G, N, 0)

    print(*res[1:-1])

#main
def main():
    # intput
    T = int(input())
    for _ in range(T): solver()

if __name__ == '__main__':
    main()