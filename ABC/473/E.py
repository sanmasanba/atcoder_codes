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
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    res = 0
    c = 0
    s = {0}
    for a in A:
        # S[l:r) = Sr - Sl より
        # Sr - Sl = 0 (mod k)
        # -> sr = sl (mod k)
        # -> そこまでにでた累積和をメモすればよい
        c = (c + a) % K
        if c in s:
            res += 1
            s = {c}
        else:
            s.add(c)
    print(res)

if __name__ == '__main__':
    main()
