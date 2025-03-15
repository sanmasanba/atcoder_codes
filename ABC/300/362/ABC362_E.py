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

def check():
    pass

#main
def main():
    # intput
    N = int(input())
    A = list(map(int, input().split()))

    dp = [[[0]*(N+1) for _ in range(N)] for _ in range(N)]

    for i in range(N+1, -1, -1):
        for j in range(i+1, N):
            dp[i][j][2] += 1
            for l in range(2, N-i):
                for k in range(j+1, N):
                    if A[k]-A[j] != A[j]-A[i]:
                        continue
                    dp[i][j][l+1] = (dp[i][j][l+1] + dp[j][k][l])%MOD998244353
    
    res = [0]*(N+1)
    res[1] = N
    for i in range(N):
        for j in range(N):
            for l in range(2, N+1-i):
                res[l] = (res[l] + dp[i][j][l])%MOD998244353
    print(*res[1:])

if __name__ == '__main__':
    main()