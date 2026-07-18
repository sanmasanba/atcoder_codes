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
    H, W, Q = map(int, input().split())
    res = [[(0, -1) for _ in range(W)] for _ in range(H)]
    res[-1][-1] = ('A', 0)

    for q in range(1, Q+1):
        R, C, X = input().split()
        R, C = int(R)-1, int(C)-1

        res[R][C] = (X, q)
    
    for h in range(H):
        for w in range(W-1, 0, -1):
            p, q = res[h][w-1], res[h][w]
            res[h][w-1] = q if p[1] < q[1] else p
    for w in range(W):
        for h in range(H-1, 0, -1):
            p, q = res[h-1][w], res[h][w]
            res[h-1][w] = q if p[1] < q[1] else p

    for r in res:
        print(''.join(rr[0] for rr in r))

if __name__ == '__main__':
    main()