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

# 291_D
# main
def main():
    # intput
    N = int(input())
    A, B = zip(*[list(map(int, input().split())) for _ in range(N)])
    
    dp = [[1, 1] for _ in range(N)]
    for i in range(N-1):
        # 表
        a = 0 if A[i] == A[i+1] else dp[i][0]
        b = 0 if B[i] == A[i+1] else dp[i][1]
        dp[i+1][0] = (a + b)%MOD998
        # 裏
        a = 0 if A[i] == B[i+1] else dp[i][0]
        b = 0 if B[i] == B[i+1] else dp[i][1]
        dp[i+1][1] = (a + b)%MOD998
    print(sum(dp[-1])%MOD998)

if __name__ == '__main__':
    main()