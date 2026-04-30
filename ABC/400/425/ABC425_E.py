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

T, M = map(int, input().split())
K = 5010
binom = [[0]*K for _ in range(K)]
binom[0][0] = 1
for n in range(1, K):
    binom[n][0] = 1
    for r in range(1, n+1):
        binom[n][r] = (binom[n-1][r]+binom[n-1][r-1])%M

def solver(M):
    N = int(input())
    C = list(map(int, input().split()))

    res = 1
    n = 0
    for c in C:
        n += c
        res = (res * binom[n][c]) % M
    print(res)

# main
def main():
    for _ in range(T):
        solver(M)
    
if __name__ == '__main__':
    main()