# library
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

# main
def main():
    # intput
    L, R, D, U = map(int, input().split())
    
    res = 0
    # |x| > |y|
    for x in range(L, R+1):
        if not x%2:
            # |x| > |y| <-> -|x| < y < |x|
            d = max(D, -abs(x)+1)
            u = min(U, abs(x)-1)
            res += max(0, u - d + 1)
    # |y| >= |x|
    for y in range(D, U+1):
        if not y%2:
            # |y| >= |x| <-> -|y| <= |x| <= |y|
            l = max(L, -abs(y))
            r = min(R, abs(y))
            res += max(0, r - l + 1)

    print(res)

if __name__ == '__main__':
    main()