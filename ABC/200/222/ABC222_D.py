#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')
MOD = 998244353

#main
def main():
    # intput
    N = int(input())
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    
    dp = [[0] * 3001 for _ in range(N+1)]
    for i in range(A[0], B[0]+1):
        dp[1][i] = 1

    for i in range(1, N):
        cumsum = [0] + list(accumulate(dp[i]))
        a, b = A[i], B[i]+1
        for c in range(a, b):
            dp[i+1][c] = cumsum[c+1]%MOD
    
    res = 0
    for i in range(3001): res = (res + dp[N][i])%MOD
    print(res)

if __name__ == '__main__':
    main()