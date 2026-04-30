# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, NamedTuple, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

# main
def main():
    # intput
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
    
    
    def bfs(s):
        dist = [0 for _ in range(N+1)]
        queue = deque()
        dist[s] = 1
        queue.append(s)
        while queue:
            v = queue.popleft()
            for next_v in G[v]:
                if dist[next_v] != 0:
                    continue
                dist[next_v] = 1
                queue.append(next_v)
        return dist
        
    print(sum(bfs(0)))

if __name__ == '__main__':
    main()