#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, List, Tuple, Dict, TypeVar, Optional
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    # input
    N, M = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    
    # dp[m][n] := m個の数字を、n桁目までで選んでときの最大値
    dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
    for m in range(M):
        for i in range(m, N):
            if m == i:
                dp[m+1][i+1] = dp[m][i] + A[i]*(m+1)
                continue
            dp[m+1][i+1] = max(dp[m][i] + A[i]*(m+1), dp[m+1][i])
    
    # output
    print(dp[M][N])

if __name__ == '__main__':
    main()