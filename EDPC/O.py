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
    A = [list(map(int, input().split())) for _ in range(N)]
    
    # dp[state] = 女性の組み合わせ状態stateの通り数
    dp = [0]*(1 << N)
    dp[0] = 1
    # すでにマッチング済みを1とした状態state
    for state in range(1, 2**N):
        # bit_count(state) := すでにマッチした男性の数
        i = state.bit_count()
        # 女性j
        for j in range(N):
            # iとjの相性がよく、マッチしている状態
            if A[i-1][j] and (state>>j)&1 == 1:
                dp[state] = (dp[state] + dp[state^(1<<j)]) % MOD1e7
    print(dp[(1 << N) - 1])

if __name__ == '__main__':
    main()