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

#main
def main():
    # intput
    N, M = map(int, input().split())
    G = defaultdict(list)
    for _ in range(M):
        s, g, weight = map(int, input().split())
        G[s-1].append((g-1, weight))
    
    res = [[False] * (1<<10) for _ in range(N)]
    res[0][0] = True
    stack = deque([(0, 0)])
    while stack:
        s, sw = stack.popleft()
        for g, w in G[s]:    
            if not res[g][sw ^ w]:
                res[g][sw ^ w] = True
                stack.append((g, sw ^ w))

    for i in range(1<<10):
        if res[N-1][i]: 
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()