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
    A, B, C, D, E, F = map(int, input().split())
    XY = set()
    for _ in range(M):
        XY.add(tuple(map(int, input().split())))

    # N = 300 -> O(N^3) <= 27 * 10**6 
    res = 1
    dp = defaultdict(int)
    dp[(0, 0)] = 1
    for _ in range(N):
        ndp = defaultdict(int)
        res = 0
        for (x, y), cnt in dp.items():
            for (dx, dy) in [(A, B), (C, D), (E, F)]:
                if (tmp := (x+dx, y+dy)) not in XY:
                    ndp[tmp] = (ndp[tmp] + cnt) % MOD998
                    res = (res + cnt) % MOD998
        dp = ndp
    print(res)

if __name__ == '__main__':
    main()
