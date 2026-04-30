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

def func(A, r):
    area = 0
    for a in A:
        if r <= a: area += (2**(2*a))
    return area

# main
def main():
    # intput
    H, W, N = map(int, input().split())
    A = list(map(int, input().split()))

    for r in range(26):
        h, w = H//(2**r), W//(2**r)
        area = h * w * (2**(2*r))

        sumarea = func(A, r)

        if area < sumarea:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()