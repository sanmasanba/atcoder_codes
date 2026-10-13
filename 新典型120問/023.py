# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, isqrt, pi, gcd, lcm, factorial
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
    A = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        G[a].append(b)
        G[b].append(a)

    w = [0]*N
    for cur in range(N):
        for nxt in G[cur]:
            w[cur] += A[nxt]

    h = []
    for i, ww in enumerate(w):
        heappush(h, (ww, -A[i], i))

    if N == 1:
        print(0)
        return

    res = 0
    used = set()
    for _ in range(N):
        while h:
            (ww, a, cur) = heappop(h)
            if w[cur] != ww:
                continue
            used.add(cur)
            for nxt in G[cur]:
                if nxt not in used:
                    heappush(h, (w[nxt]+a, -A[nxt], nxt))
                    w[nxt] += a
            res = max(res, ww)
            break
    print(res)

if __name__ == '__main__':
    main()
