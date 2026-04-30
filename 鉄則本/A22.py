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
    B = list(map(int, input().split()))
    
    dp = [-1]*(N+1)
    dp[1] = 0
    for i in range(1, N):
        if dp[i] == -1: continue
        dp[A[i-1]] = max(dp[A[i-1]], dp[i]+100)
        dp[B[i-1]] = max(dp[B[i-1]], dp[i]+150)

    print(dp[N])

if __name__ == '__main__':
    main()