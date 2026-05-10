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
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split(' '))
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    
    dist = [-1] * N
    dist[0] = 0
    que = deque(G[0])
    for v in G[0]:
        dist[v] = 1
    while que:
        v = que.popleft()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = v + 1
                que.append(nv)
            
    if all(map(lambda x: x != -1, dist)):
        print('Yes')
        print(*dist[1:], sep='\n')
    else:
        print('No')

if __name__ == '__main__':
    main()