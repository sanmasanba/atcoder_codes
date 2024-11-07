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
    N, M = map(int, input().split(' '))
    global G
    G = [set() for _ in range(N)]
    for _ in range(M):
        k = int(input())
        A = list(map(int, input().split(' ')))
        for i in range(k-1):
            G[A[i+1]-1].add(A[i]-1)

    # topo_sort
    topo_sort = []
    ind = [0] * N
    for v in range(N):
        for nv in G[v]:
            ind[nv] += 1
    que = deque()
    for v in range(N):
        if not ind[v]:
            que.append(v)
    while que:
        v = que.popleft()
        topo_sort.append(v)
        for nv in G[v]:
            ind[nv] -= 1
            if ind[nv] == 0:
                que.append(nv)
    
    print("Yes" if len(topo_sort) == N else "No")

if __name__ == '__main__':
    main()