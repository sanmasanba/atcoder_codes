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
    G = {i:[] for i in range(N+1)}
    for i in range(1, N+1):
        _, *p = map(int, input().split(' '))
        G[i] = p

    res = []
    seen = set()
    def dfs(v): 
        seen.add(v)       
        for nv in G[v]:
            if nv in seen:
                continue
            dfs(nv)
        res.append(v)
                
    dfs(1)
    res.pop()
    print(*res)

if __name__ == '__main__':
    main()