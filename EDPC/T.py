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
    S = list(input().strip())
    
    # dp[i][j] := ボールがi個置かれていて、文字iが書かれたボールが
    #             左からj番目に挿入されている場合の数
    dp = [[0]*3001 for _ in range(3001)]
    dp[1][1] = 1
    
    for i in range(1, N):
        if S[i-1] == '<':
            # 挿入位置jから見ると、jより左側にiがある場合の数は
            # 単調増加になっている　→　先頭からいもす法
            sumv = 0
            for j in range(1, i+1):
                sumv = (sumv + dp[i][j]) % MOD1e7
                dp[i+1][j+1] = (dp[i+1][j+1] + sumv) % MOD1e7
        else:
            # 挿入位置jから見ると、jより右側にiがある場合の数は
            # 単調増加になっている　→　末尾からいもす法
            sumv = 0
            for j in range(i, 0, -1):
                sumv = (sumv + dp[i][j]) % MOD1e7
                dp[i+1][j] = (dp[i+1][j] + sumv) % MOD1e7
    res = 0
    for i in range(1, N+1): res = (res + dp[N][i]) % MOD1e7
    print(res)

if __name__ == '__main__':
    main()