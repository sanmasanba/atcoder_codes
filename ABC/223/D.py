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
    G = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split(' '))
        G[a].add(b)
    
    # topo_sort
    topo_sort = []
    ind = [0] * N
    for v in range(N):
        for nv in G[v]:
            ind[nv] += 1
    que = []
    for v in range(N):
        if ind[v] == 0:
            que.append(v)
    while que:
        v = heappop(que)
        topo_sort.append(v+1)
        for nv in G[v]:
            ind[nv] -= 1
            if ind[nv] == 0:
                heappush(que, nv)
    # 閉路がある場合は、条件を満たせない
    if len(topo_sort) != N:
        print(-1)
        return
    print(*topo_sort)

if __name__ == '__main__':
    main()