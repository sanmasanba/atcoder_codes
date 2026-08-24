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
    N, M, K = map(int, input().split())

    dp = [1] * (M+1)
    dp[0] = 0
    for _ in range(1, N):
        ndp = [0]*(M+1)
        cumsum = [0] + list(accumulate(dp))
        if K == 0:
            ndp = [cumsum[-1]%MOD998] * (M+1)
            ndp[0] = 0
        else:
            for i in range(1, M+1):
                tmp = 0
                if 0 <= i-K+1:
                    tmp = (tmp + cumsum[i-K+1]) % MOD998
                if i+K < len(cumsum):
                    tmp = ((cumsum[-1] - cumsum[i+K]) % MOD998 + tmp ) % MOD998
                ndp[i] = tmp
        dp = ndp

    res = 0
    for x in dp: res = (res + x) % MOD998
    print(res)

if __name__ == '__main__':
    main()
