#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    # intput
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    r = 0
    SUM = 0
    res = 0
    for l in range(N):
        while r < N and SUM < K:
            SUM += A[r]
            r += 1
        if K <= SUM:
            res += N+1- r

        if r == l:
            r += 1
        SUM -= A[l]
    
    print(res)

if __name__ == '__main__':
    main()