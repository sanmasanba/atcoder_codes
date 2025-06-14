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

#prime_factorization
def prime_factorization(N) -> list:
    res = []
    for p in range(2, N):
        if p * p > N:
            break
        if N % p != 0:
            continue
        e = 0
        while N % p == 0:
            e += 1
            N //= p
        res.append((p, e))
        if 2 < len(res):
            return False
    if N != 1:
        res.append((N, 1))
    return len(res) == 2

from math import isqrt

#main
def main():
    # intput
    Q = int(input())
    P = [p**2 for p in range(6, 10**6) if prime_factorization(p)]

    print(len(P))

    for _ in range(Q):
        A = int(input())        
        for p in P:
            break
    

if __name__ == '__main__':
    main()