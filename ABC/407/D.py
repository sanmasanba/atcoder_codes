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

#main
def main():
    # intput
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    
    global res, grid
    grid = 0
    res = 0
    for i in range(H):
        for j in range(W):
            res ^= A[i][j]
    
    memo = set()
    def dfs(crr):
        global res, grid
        res = max(res, crr)
        if grid in memo:
            return

        for i in range(H):
            for j in range(W):
                # 設置済みはスルー
                if grid >> (i*W+j) & 1:
                    continue
                # 縦置き
                crr ^= A[i][j]
                grid ^= 1 << (i*W+j)
                if i+1 < H and not (grid >> ((i+1)*W+j) & 1):
                    grid ^= 1 << ((i+1)*W+j)
                    dfs(crr ^ A[i+1][j])
                    memo.add(grid)
                    grid ^= 1 << ((i+1)*W+j)
                # 縦置き
                if j+1 < W and not (grid >> (i*W+j+1) & 1):
                    grid ^= 1 << (i*W+j+1)
                    dfs(crr ^ A[i][j+1])
                    memo.add(grid)
                    grid ^= 1 << (i*W+j+1)
                crr ^= A[i][j]
                grid ^= 1 << (i*W+j)
    dfs(res)
    print(res)

if __name__ == '__main__':
    main()