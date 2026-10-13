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
    N, Q = map(int, input().split())
    P = list(map(int, input().split()))
    rank = [0]*N
    for r, p in enumerate(P):
        rank[p-1] = r

    for _ in range(Q):
        a = int(input()) - 1
        rank[a] = N
        N += 1
    tmp = [(a, r) for a, r in enumerate(rank)]
    tmp.sort(key=lambda x: x[1])
    print(' '.join(str(a+1) for a, _ in tmp))

if __name__ == '__main__':
    main()
