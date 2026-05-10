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
    N = int(input())
    M = [[0]*2001 for _ in range(2001)]
    A = [0] * N
    U, D, L, R = zip(*[list(map(lambda x: int(x)-1, input().split())) for _ in range(N)])
    for i, (u, d, l, r) in enumerate(zip(U, D, L, R)):
        A[i] = (d-u+1)*(r-l+1)
        M[u][l] += 1
        M[d+1][l] -= 1
        M[u][r+1] -= 1
        M[d+1][r+1] += 1
    
    for i in range(2000):
        for j in range(2000):
            M[i][j+1] += M[i][j]
    for i in range(2000):
        for j in range(2000):
            M[i+1][j] += M[i][j]

    s = 0
    for i in range(2000):
        for j in range(2000):
            if 0 < M[i][j]:
                s += 1
                M[i][j] = min(2, M[i][j])
    
    M = cumsum2d(M)
    for a, u, d, l, r in zip(A, U, D, L, R):
        b = M[d+1][r+1] - M[u][r+1] - M[d+1][l] + M[u][l]
        print(4000000 - (s - 2*a + b))
 
if __name__ == '__main__':
    main()