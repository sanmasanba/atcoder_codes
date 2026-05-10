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
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    res = [0]*Q
    for q in range(Q):
        X, Y = map(int, input().split())
        ng = X-1
        ok = 3 * 10 ** 9 + 5
        s = bisect_left(A, X)
        while ok-ng>1:
            mi = (ng+ok)//2
            t = bisect_right(A, mi, lo=s)
            n = (mi - X + 1) - (t - s)
            if Y <= n:
                ok = mi
            else:
                ng = mi
        res[q] = str(ok)
    print("\n".join(res))

if __name__ == '__main__':
    main()