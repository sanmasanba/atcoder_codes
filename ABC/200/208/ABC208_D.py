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
    G = [[INF] * N for _ in range(N)]
    for _ in range(M):
        s, g, weight = map(int, input().split(' '))
        G[s-1][g-1] = weight

    res = 0
    for i in range(N): G[i][i] = 0
    for k in range(N):
        for s in range(N):
            for t in range(N):
                G[s][t] = min(G[s][t], G[s][k] + G[k][t])
        for i in range(N):
            for j in range(N):
                res += 0 if G[i][j] == INF else G[i][j]
    
    print(res)

if __name__ == '__main__':
    main()