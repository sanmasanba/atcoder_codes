#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')
def func(l, r, flag, N, A, dp):
    # 計算済みなら、メモを返す
    if dp[l][r] != -1:
        return dp[l][r]
    # 最後のひとかけら
    if l == r:
        # IOIちゃんの番ならケーキは取れない
        if flag:
            dp[l][r] = 0
        # JOI君の番なら最後のケーキを取る
        else:
            dp[l][r] = A[l]
        return dp[l][r]
    # IOIちゃんのターン
    if flag:
        # 大きいほうを取る
        if A[l] > A[r]:
            dp[l][r] = func((l+1)%N, r, 0, N, A, dp)
        else:
            dp[l][r] = func(l, (r+N-1)%N, 0, N, A, dp)
        return dp[l][r]
    # JOIくんのターン
    # 大きいほうを返す
    dp[l][r] = max(func((l+1)%N, r, 1, N, A, dp)+A[l], func(l, (r+N-1)%N, 1, N, A, dp)+A[r])
    return dp[l][r]

#main
def main():
    N = int(input())
    A = []
    for _ in range(N):
        a = int(input())
        A.append(a)
    
    # 区間DP
    dp = [[-1]*2010 for _ in range(2010)]

    res = 0
    # JOI君が最初にとるケーキをiとする
    for i in range(N):
        # i番目のケーキを取って、IOIちゃんのターンにまわす
        # [0, 1, ..., i, ..., N]を[i+1, i+2, ..., N, 0, 1, ..., i-1]を渡す。
        res = max(res, func((i+1)%N, (i+N-1)%N, 1, N, A, dp) + A[i])

    print(res)


if __name__ == '__main__':
    main()