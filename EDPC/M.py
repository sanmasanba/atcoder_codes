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
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    # dp[i][j] := 人iまでに合計j個の飴を配る方法の数
    dp = [0]*500001
    dp[0] = 1
    for i in range(N):
        # 人iが最大でai個配れるとき、人iまでにj個配り終わるには
        # 人i-1までに、j-k, j-k+1, ..., j-1, j個は配っている
        cumsum = [0] + list(accumulate(dp, func=lambda x, y: (x+y)%MOD1e7))
        for j in range(K+1):
            dp[j] = (cumsum[j+1] - cumsum[max(0, j-A[i])]) % MOD1e7

    print(dp[K])

if __name__ == '__main__':
    main()