# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, isqrt, pi, gcd, lcm, factorial
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

# main
def main():
    # intput
    N, W = map(int, input().split())
    A, B = map(list, zip(*[list(map(int, input().split())) for _ in range(N)]))

    res = 0
    # bit_search
    res = 0
    for mask in range(1 << N):
        # 部分集合ごとの判定用の値を初期化
        total = 0
        w = 0
        for i in range(N):
            if mask >> i & 1:
                total += A[i]
                w += B[i]
        if w <= W:
            res = max(res, total)
    
    print(res)

if __name__ == '__main__':
    main()
