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
MOD998244353 = 998244353
MOD1000000007 = 1000000007

#main
def main():
    # intput
    N = int(input())
    A = list(map(int, input().split()))
    
    l_dp = [[0]*2 for _ in range(N+1)]
    r_dp = [[0]*2 for _ in range(N+1)]
    l_dp[0][1] = A[-1]
    r_dp[0][1] = A[0]

    for i in range(N):
        l_dp[i+1][0] = l_dp[i][1]
        l_dp[i+1][1] = min(l_dp[i][1], l_dp[i][0]) + A[i]
    A = A[::-1]
    for i in range(N):
        r_dp[i+1][0] = r_dp[i][1]
        r_dp[i+1][1] = min(r_dp[i][1], r_dp[i][0]) + A[i]

    print(min(min(l_dp[-1]), min(r_dp[-1])))

if __name__ == '__main__':
    main()