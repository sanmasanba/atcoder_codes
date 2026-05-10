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
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    
    dp = [[-1]*D for _ in range(K+1)]
    dp[0][0] = 0
    for k in range(K):
        for d in range(D):
            if dp[k][d] < 0:
                continue
            d = dp[k][d] * D + d
            for i in range(N-(K-1-k)):
                tmp = d + A[i]
                p, q = tmp//D, tmp%D
                dp[k+1][q] = max(dp[k+1][q], p)

    if dp[K][0] < 0:
        print(-1)
    else:
        print(dp[K][0]*D)

if __name__ == '__main__':
    main()