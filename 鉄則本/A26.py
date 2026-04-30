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

# eratosthenes
def eratosthenes(N: int) -> List[int]:
    isprime = [True] * (N+1)

    isprime[0], isprime[1] = False, False

    for p in range(2, N+1):
        if not isprime[p]:
            continue

        q = p * 2
        while q <= N:
            isprime[q] = False
            q += p

    return isprime

#main
def main():
    # intput
    Q = int(input())

    e =eratosthenes(300001)
    for _ in range(Q):
        print('Yes' if e[int(input())] else 'No')

if __name__ == '__main__':
    main()