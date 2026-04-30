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
    c = [list(input().strip()) for _ in range(H)]

    dp = [[0]*W for _ in range(H)]
    dp[0][0] = 1

    for i in range(H):
        for j in range(W):
            if c[i][j] == '#' or (i, j) == (0, 0): continue
            a, b = 0, 0
            if 0 < i: a = dp[i-1][j]
            if 0 < j: b = dp[i][j-1]
            dp[i][j] = a + b

    print(dp[-1][-1])

if __name__ == '__main__':
    main()