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
    # Step1. Input
    N = int(input())
    A = list(map(int, input().split()))
    dp = [[INF] * (2 * N) for _ in range(2 * N)]

    # Step2. Initialize
    for i in range(2 * N - 1):
        dp[i][i + 1] = abs(A[i + 1] - A[i])

    # Step3. DP
    for length in range(3, 2 * N, 2):
        for left in range(2 * N - length):
            right = left + length
            for k in range(left, right):
                dp[left][right] = min(dp[left][right], dp[left][k] + dp[k + 1][right])
            dp[left][right] = min(dp[left][right], 
                                  dp[left + 1][right - 1] + abs(A[left] - A[right]))

    # Step #4. Output
    print(dp[0][2*N-1])

if __name__ == '__main__':
    main()