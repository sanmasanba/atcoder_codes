#library
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

#main
def main():
    # intput
    H, W, N = map(int, input().split())
    grid = [[0]*(W+1) for _ in range(H+1)]
    for _ in range(N):
        a, b, c, d = map(lambda x: int(x)-1, input().split())
        grid[a][b] += 1
        grid[a][d+1] -= 1
        grid[c+1][b] -= 1
        grid[c+1][d+1] += 1
    
    cumsum = cumsum2d(grid)
    for c in cumsum[1:-1]:
        print(*c[1:-1])

if __name__ == '__main__':
    main()