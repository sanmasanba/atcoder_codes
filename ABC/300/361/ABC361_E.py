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
    N = int(input())
    G = defaultdict(list)
    for _ in range(N-1):
        s, g, weight = map(int, input().split())
        G[s].append((g, weight))
        G[g].append((s, weight))
    
    seen = [0]*(N+1)
    dist_from_0 = [0]*(N+1)
    def dfs(v, dist):
        seen[v] = 1
        dist_from_0[v] = dist
        for next_v, weight in G[v]:
            if seen[next_v]:
                continue
            dfs(next_v, dist+weight)
        seen[v] = 0

    dfs(1, 0)
    print(dist_from_0)

    

if __name__ == '__main__':
    main()