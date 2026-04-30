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

def func(A, B):
    tmp = set()
    for a, b in zip(A, B):
        tmp.add(a)
        tmp.add(a+b)
    tmp = sorted(list(tmp))
    d2i, i2d = {}, {}
    for i, d in enumerate(tmp):
        d2i[d] = i
        i2d[i] = d
    return d2i, i2d, tmp

# main
def main():
    # intput
    N = int(input())
    A, B = zip(*[list(map(int, input().split())) for _ in range(N)])
    
    d2i, i2d, days = func(A, B)
    memo = [0]*(len(d2i))
    for a, b in zip(A, B):
        memo[d2i[a]] += 1
        memo[d2i[a+b]] -= 1
    cumsum = [0] + list(accumulate(memo))
    res = [0]*(N+1)
    for i in range(len(days)-1):
        res[cumsum[i+1]] += days[i+1] - days[i]
    print(*res[1:])

if __name__ == '__main__':
    main()