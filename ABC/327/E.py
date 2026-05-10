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
input = sys.stdin.readline

#main
def main():
    BASE = 10**7
    # intput
    N = int(input())
    P = list(map(int, input().split()))
    P = P[::-1]

    # dp[i][j] := i個のコンテストに出た時、i番目のコンテストに
    #             コンテストjを選んだ時のレート
    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):    
        for j in range(i, N):
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j]+P[j]*BASE*(0.9**i))
    
    res = -INF
    denominator = 0
    for k, d in enumerate(dp[1:]):
        tmp = d[-1]
        denominator += BASE*(0.9**k)
        root_k = BASE*(1200/sqrt(k+1))
        res = max(res, tmp/denominator - root_k/BASE)
    print(res)

if __name__ == '__main__':
    main()