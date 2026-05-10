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
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split(' '))
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    
    # DFS
    L = [0]*N
    R = [0]*N
    global x
    x = 1 
    def dfs(v, p=-1):
        global x
        L[v] = x
        for next_v in G[v]:
            if next_v == p:
                continue
            dfs(next_v, v)
        # 始めてきた葉ならインクリメント
        if len(G[v]) == 1 and p != -1:
            x += 1
        # 戻り掛けで区間を記述
        R[v] = x-1 
    dfs(0)

    for l, r in zip(L, R):
        print(l, r)

if __name__ == '__main__':
    main()