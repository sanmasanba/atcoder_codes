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

def cumsum2d(a:List[T]) -> List[T]:
    h, w = len(a), len(a[0])
    tmp = [[0] * (w+1) for _ in range(h+1)]
    for i in range(h):
        for j in range(w):
            tmp[i+1][j+1] = (
                tmp[i+1][j]
                + tmp[i][j+1]
                - tmp[i][j]
                + a[i][j]
                )
    return tmp

# main
def main():
    # intput
    H, W, K = map(int, input().split())
    S = [list(map(int, list(input().strip()))) for _ in range(H)]
    
    c = cumsum2d(S)

    def f(r1, c1, r2, c2):
        return c[h][w] - c[i][w] - c[h][j] + c[i][j]

    res = 0
    for h in range(1, H+1):
        for w in range(1, W+1):
            for i in range(h):
                if f(h, w, i, 0) < K or K < f(h, w, i, w-1):
                    continue
                
    print(res)

if __name__ == '__main__':
    main()