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
MOD998244353 = 998244353
MOD1000000007 = 1000000007

#main
def main():
    # intput
    N, M = map(int, input().split())
    G = defaultdict(list)
    for _ in range(M):
        s, g, weight = map(int, input().split())
        G[s].append((g, weight))
        G[g].append((s, weight))
    
    # DFS
    global res
    res = INF
    seen = set()
    def dfs(v, n, ans):
        global res
        seen.add(v)
        for next_v, label in G[v]:
            if next_v in seen:
                continue
            ans ^= label
            if next_v == n:
                res = min(res, ans)
            else:
                dfs(next_v, n, ans)
            ans ^= label
        seen.remove(v)
    
    dfs(1, N, 0)
    print(res)

if __name__ == '__main__':
    main()