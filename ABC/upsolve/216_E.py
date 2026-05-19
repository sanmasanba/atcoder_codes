# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop, heapify
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

def _calc(a):
    return (a*(a+1))//2

def calc(a, m):
    return _calc(-a) - _calc(-(a+m))

# main
def main():
    # intput
    N, K = map(int, input().split())
    A = list(map(lambda x: -int(x), input().split()))
    tmp = defaultdict(int)
    for a in A: tmp[a] += 1
    A = [(a, cnt) for a, cnt in tmp.items()]
    heapify(A)
    
    res = 0
    while K:
        (a, a_cnt) = heappop(A)
        if K < a_cnt:
            res -= a * min(a_cnt, K)
            break

        if not A:
            m = min(-a, K//a_cnt)
            res += calc(a, m) * a_cnt
            a += m
            K -= m * a_cnt
            if 0 <= K < a_cnt:
                res -= a * K
            break
        else:
            (b, b_cnt) = heappop(A)
            n = b-a
            m = min(n, K//a_cnt)
            res += calc(a, m) * a_cnt
            a += m
            K -= m * a_cnt
            if a < b:
                heappush(A, (a, a_cnt))
                heappush(A, (b, b_cnt))
            else:
                heappush(A, (b, a_cnt+b_cnt))
    print(res)


if __name__ == '__main__':
    main()