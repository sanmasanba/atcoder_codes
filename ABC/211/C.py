#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

# ライブラリはここに貼り付け

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    i2c = {i:c for i, c in enumerate('chokudai')}
    S = list(input())
    N = len(S)
    dp = [[0]*(N+1) for _ in range(9)]
    # cのリストだけ更新
    for j in range(N):
            if S[j] == "c":
                dp[1][j+1] = dp[1][j]+1
            else:
                dp[1][j+1] = dp[1][j]
    # dpをする
    for i in range(1, 8):
        for j in range(N):
            # 文字が一致するとき、既存の組み合わせ+新しいやつ
            if S[j] == i2c[i]:
                dp[i+1][j+1] = dp[i][j]+dp[i+1][j]
            # 既存の組み合わせから増えない
            else:
                dp[i+1][j+1] = dp[i+1][j]
    print(dp[8][N]%(10**9+7))

if __name__ == '__main__':
    main()