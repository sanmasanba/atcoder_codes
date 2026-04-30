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
    
    r = 0
    sum, res = 0, 0
    for l in range(N):
        while r < N and sum + A[r] <= K:
            sum += A[r]
            r += 1
        res += r - l
        sum -= A[l]
    print(res)

if __name__ == '__main__':
    main()