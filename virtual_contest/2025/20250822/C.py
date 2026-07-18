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

# prime_factorization
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
    if N != 1:
        res.append((N, 1))
    return res

# main
def main():
    # intput
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    memo = set()
    res = [1]*(M+1)
    res[0] = 0
    for a in A:
        if a == 1: continue
        for (n, _) in prime_factorization(a):
            memo.add(n)
    for p in memo:
        q = p
        while p <= M:
            res[p] = 0
            p += q
    print(sum(res))
    for i, r in enumerate(res):
        if r == 1: print(i)

if __name__ == '__main__':
    main()