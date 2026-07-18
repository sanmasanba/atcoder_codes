# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, NamedTuple, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

# main
def main():
    # intput
    N, K = map(int, input().split())
    C = []
    for _ in range(N):
        C.append(list(map(int, input().split())))
    
    # dp[i][j][k] := k回flipした状態で、j枚目をi(表or裏)とする
    dp = [[[-1]*(2*K+1) for _ in range(2)] for _ in range(N+1)]
    dp[0][0][0] = 0
    # flipなしのパターン
    for i in range(N):
        dp[i+1][0][0] = dp[i][0][0] + C[i][0]
    
    # i枚目を決める
    for i in range(N):
        # k回flipしたシチュを考える
        for k in range(2*K):
            # k回flipしたあとが表か裏か
            for j in range(2):
                # i+1枚目がjでk+1回めくられているパターンは
                # [i,^j,k]からflip, [i,j,k+1]からそのまま の2パターンからくる
                a = -1 if dp[i][(j+1)%2][k] < 0 else (dp[i][(j+1)%2][k] + C[i][j])
                b = -1 if dp[i][j][k+1] < 0 else (dp[i][j][k+1] + C[i][j])
                dp[i+1][j][k+1] = max(dp[i+1][j][k+1], a, b)
        
    res = -1
    for tmp in dp[-1]:
        res = max(res, *tmp)
    print(res)

if __name__ == '__main__':
    main()