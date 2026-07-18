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
    N, K = map(int, input().split())
    S = list(map(str, input().split()))
    
    tmp = runlength_encoding(S)
    res = []
    for c, v in tmp:
        if v >= K: res.extend([c]*v)
    print(*res)

if __name__ == '__main__':
    main()
