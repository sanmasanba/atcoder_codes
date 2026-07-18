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

def runlength_encoding(raw: Iterable[T]) -> List[Tuple[T, int]]:
    l, n = 0, len(raw)
    res = []
    while l < n:
        r = l + 1
        while r < n and raw[l] == raw[r]:
            r += 1
        res.append((raw[l], r - l))
        l = r
    return res

# main
def main():
    # intput
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    res = []
    a = A[:]
    for i in range(N-1):
        aij = (a[i] + a[i+1])%2
        if aij != B[i]:
            res.append(1)
        else:
            res.append(0)
    
    res = runlength_encoding(res)
    ret = 0
    for a, c in res:
        if a == 1:
            ret += (c+1)//2
    print(ret)

if __name__ == '__main__':
    main()