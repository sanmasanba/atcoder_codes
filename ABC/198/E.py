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
    C = list(map(lambda x: int(x)-1, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(lambda x: int(x)-1, input().split())
        G[a].append(b)
        G[b].append(a)
    
    res = []
    seen_color = [0]*(10**5)
    seen = [0]*N
    def dfs(v):
        # update
        seen[v] = 1
        if not seen_color[C[v]]:
            res.append(v+1)
        seen_color[C[v]] += 1
        
        # search    
        for next_v in G[v]:
            if seen[next_v]:
                continue
            dfs(next_v)
        
        # update
        seen[v] = 0
        seen_color[C[v]] -= 1
    
    dfs(0)
    print(*sorted(res))

if __name__ == '__main__':
    main()