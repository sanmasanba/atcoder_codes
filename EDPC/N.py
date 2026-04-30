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
    N = int(input())
    A = list(map(int, input().split()))
    cumsum = [0] + list(accumulate(A))

    dp = [[INF]*(N+1) for _ in range(N+1)]
    for i in range(N): dp[i][i+1] = 0
    for length in range(2, N+1):
        for l in range(N+1-length):
            r = l + length
            for sep in range(l+1, r):
                cost = (cumsum[sep]- cumsum[l]
                        + cumsum[r] - cumsum[sep])
                dp[l][r] = min(dp[l][r], 
                               dp[l][sep]+dp[sep][r]+cost)
    print(dp[0][N])

if __name__ == '__main__':
    main()