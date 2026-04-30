#library
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

#main
def main():
    # intput
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    def search(l):
        L, r = A[l], N
        while l+1 < r:
            m = (l+r)//2
            diff = A[m]-L
            if diff <= K:
                l = m
            else:
                r = m
        return r - 1

    res = 0
    for l in range(N-1):
        res += search(l) - l 
    print(res)

if __name__ == '__main__':
    main()