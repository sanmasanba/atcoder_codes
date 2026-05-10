#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, List, Tuple, Dict, TypeVar, Optional
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, M = map(int, input().split(' '))
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split(' '))
        G[a-1].append(b-1)
    
    dist = [INF] * N
    dist[0] = 0
    Q = deque([0])

    while len(Q) > 0:
        v = Q.popleft()
        for next_v in G[v]:
            if next_v == 0:
                print(dist[v] + 1)
                return
            if dist[next_v] == INF:
                dist[next_v] = dist[v] + 1
                Q.append(next_v)
    
    print(-1)

if __name__ == '__main__':
    main()