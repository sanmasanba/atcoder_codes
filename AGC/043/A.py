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

#main
def main():
    # intput
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    # dp[i][j][k] := 反転しているか(i)どうかの状態から、マス(j, k)に
    #                たどりつくことのできる最小の反転回数
    dp = [[[INF]*(W+1) for _ in range(H+1)] for _ in range(2)]
    dp[0][1][0] = 0
    dp[0][0][1] = 0
    dp[1][1][0] = 1
    dp[1][0][1] = 1

    for j in range(H):
        for k in range(W):
            # 反転なし
            # 0 -> 0
            a = INF if S[j][k] == '#' else dp[0][j][k+1]
            b = INF if S[j][k] == '#' else dp[0][j+1][k]
            # 1 -> 0
            c = INF if S[j][k] == '#' else dp[1][j][k+1]
            d = INF if S[j][k] == '#' else dp[1][j+1][k]
            dp[0][j+1][k+1] = min(a, b, c, d)

            # 反転あり
            # 0 -> 1
            a = INF if S[j][k] == '.' else dp[0][j][k+1] + 1
            b = INF if S[j][k] == '.' else dp[0][j+1][k] + 1
            # 1 -> 1
            c = INF if S[j][k] == '.' else dp[1][j][k+1]
            d = INF if S[j][k] == '.' else dp[1][j+1][k]
            dp[1][j+1][k+1] = min(a, b, c, d)
    
    print(min(dp[0][-1][-1], dp[1][-1][-1])) 
    bisect_left()

if __name__ == '__main__':
    main()