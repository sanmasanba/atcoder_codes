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

# main
def main():
    # intput
    N, W = map(int, input().split())
    w, v = zip(*[list(map(int, input().split())) for _ in range(N)])
    
    dp = [-1]*(W+1)
    dp[0] = 0
    for i in range(N):
        ndp = dp[:]
        item_w, item_v = w[i], v[i]
        for w_ in range(W):
            if W < w_+item_w or dp[w_] < 0:
                continue

            ndp[w_+item_w] = max(ndp[w_+item_w], dp[w_] + item_v)
        dp = ndp
    print(max(dp))

if __name__ == '__main__':
    main()