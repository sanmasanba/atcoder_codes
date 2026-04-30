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
    G = [[0]*N for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        G[a][b] = 1
        G[b][a] = 1
    
    # 頂点を全列挙する
    res = INF
    edges = [(i, j) for i in range(N) for j in range(i+1, N)]
    for e in combinations(edges, N):
        deg = [0] * N
        # tmp := 対象の辺のうちすでにある辺を記録
        tmp = 0
        for u, v in e:
            deg[u] += 1
            deg[v] += 1
            tmp += G[u][v]
        if all(d == 2 for d in deg):
            # N-tmp: 今ない辺に追加した辺を足す
            # M-tmp: 今ある辺から追加したい辺を引く
            res = min(res, N+M-2*tmp)
    print(res)

if __name__ == '__main__':
    main()