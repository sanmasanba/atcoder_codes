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

def f(m, co, A, B, x, y):
    res = 2*(A*m + B*(co - m))
    t = abs(x - y)
    if x > y:
        res += A*(t//2) + B*(t - t//2)
    else:
        res += B*(t//2) + A*(t - t//2)
    return res

def solve():
    A, B, X, Y = map(int, input().split())
    x, y = abs(X), abs(Y)
    if A == B:
        print(A*x + B*y)
        return
    
    co = min(x, y)
    l = 0
    r = co
    while r-l > 100:
        m1 = (2*l+r)//3
        m2 = (l+2*r)//3
        c1 = f(m1, co, A, B, x, y)
        c2 = f(m2, co, A, B, x, y)
        if c1 > c2: l = m1
        else: r = c2
    res = INF
    for i in range(l, r+1):
        res = min(res, f(i, co, A, B, x, y))
    print(res)

# main
def main():
    # intput
    N = int(input())
    for _ in range(N):
        solve()

if __name__ == '__main__':
    main()