# library
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

# main
def main():
    # intput
    N = int(input())
    G = [set() for _ in range(N)]
    ok = [0]*N
    edges = []
    q = []
    for i in range(N):
        a, b = map(lambda x: int(x)-1, input().split())
        edges.append((a, b))
        if a == -1 and b == -1:
            ok[i] = 1
            q.append(i)
        else:
            G[a].add(i)
            G[b].add(i)
    
    seen = [0]*N
    while q:
        x = q.pop()
        for y in G[x]:
            if seen[y]: continue
            seen[y] = 1
            q.append(y)
            ok[y] = 1
    print(sum(ok))

if __name__ == '__main__':
    main()