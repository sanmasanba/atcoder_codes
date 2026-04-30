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

def rle(S):
    res = []
    for c in S:
        if res and res[-1][0] == c:
            res[-1][1] += 1
        else:
            res.append([c, 1])
    return res
    
def solver():
    N = int(input())
    S = list(input().strip())    
    
    r = rle(S)
    if len(r) == 1:
        print(0)
        return
    
    cnt0, cnt1 = 0, 0
    for (c, cnt) in r:
        if c == '0': cnt0 += cnt
        else: cnt1 += cnt

    res = INF
    for (c, cnt) in r:
        tmp0, tmp1 = cnt0 - (cnt if c == '0' else 0), cnt1 - (cnt if c == '1' else 0)
        res = min(res, tmp0 * (2 if c == '0' else 1) + tmp1 * (2 if c == '1' else 1))
    print(res)
    return

# main
def main():
    # intput
    T = int(input())
    for _ in range(T): solver()

if __name__ == '__main__':
    main()