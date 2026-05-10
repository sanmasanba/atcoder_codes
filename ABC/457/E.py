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

def solve(N, l2r ,r2l):
    S, T = map(lambda x: int(x), input().split())
    

# main
def main():
    # intput
    N, M = map(int, input().split())
    l2r, r2l = defaultdict(lambda: 0), defaultdict(lambda: INF)
    for _ in range(M):
        l, r = map(int, input().split())
        l2r[l] = max(r, l2r.get(l))
        r2l[r] = min(l, r2l.get(r))
    Q = int(input())    
    for _ in range(Q):
        solve(N, l2r, r2l)

if __name__ == '__main__':
    main()