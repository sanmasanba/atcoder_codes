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

# 考察
# P(n)=A^n、S(n)=1+A+...+A^(n-1) を同時に求める。
#
# 長さ  | べき乗     | 等比和            |
# 2k    | P(k)^2    | S(k) × (1 + P(k)) |
# 2k+1  | P(2k) × A | S(2k) + P(2k)     |
#
# 再帰で n//2 を先に解けば、毎回項数が半分になり O(log X)

@lru_cache
def s_k(a, x, m):
    if x <= 0:
        return 0
    
    if x%2 == 0:
        return (s_k(a, x//2, m) * (1 + p_k(a, x//2, m))) % m
    else:
        return (s_k(a, x-1, m) + p_k(a, x-1, m)) % m

@lru_cache
def p_k(a, x, m):
    if x == 0:
        return 1
    
    if x%2 == 0:
        return (p_k(a, x//2, m) * p_k(a, x//2, m)) % m
    else:
        return (a * p_k(a, x-1, m)) % m

# main
def main():
    # intput
    A, X, M = map(int, input().split())

    print(s_k(A, X, M))

if __name__ == '__main__':
    main()
