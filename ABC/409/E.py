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
    N = int(input())
    X = list(map(int, input().split()))
    G = defaultdict(list)
    for _ in range(N-1):
        s, g, weight = map(int, input().split())
        G[s].append((g, weight))
        G[g].append((s, weight))
    
    # DFS
    global res
    res = 0
    seen = set()
    def dfs(v=1):
        global res
        seen.add(v)
        for next_v, weight in G[v]:
            if next_v in seen:
                continue
            if len(G)!=1: dfs(next_v)
            res += weight * abs(X[next_v-1])
            X[v-1] += X[next_v-1]
        seen.remove(v)
        return res
    dfs()
    print(res)

if __name__ == '__main__':
    main()