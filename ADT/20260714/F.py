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
    N, A, B = map(int, input().split())
    S = list(input())
    a, b = [1 if i=='a' else 0 for i in S], [1 if i=='b' else 0 for i in S]
    cA = [0] + list(accumulate(a))
    cB = [0] + list(accumulate(b))

    res = 0
    r = 0
    for l in range(N):
        while r < N and cB[r+1]-cB[l] < B:
            r += 1
        if cA[r]-cA[l] < A:
            continue
        ng = l
        ok = r
        while ok-ng>1:
            m = (ok+ng)//2
            if cA[m]-cA[l] < A:
                ng = m
            else:
                ok = m
        res += r-ok+1
    print(res)

if __name__ == '__main__':
    main()