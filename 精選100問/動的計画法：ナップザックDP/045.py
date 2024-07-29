#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

def round255(N):
    return min(255, max(0, N))

#main
def main():
    res = []
    while 1:
        N, M = map(int, input().split(' '))
        # 終了命令
        if N == 0 and M == 0:
            break
        C = [int(input()) for _ in range(M)]
        X = [int(input()) for _ in range(N)]

        # N+1個のdpを考える
        # dp[x_i][y_iの変換後] = y_iまでの総和
        dp = [[INF]*256 for i in range(N+1)]
        # y0(=128)の二乗和を0とする
        dp[0][128] = 0

        # xとx+1でdp
        for x in range(N):
            # 変換後の値をループ
            for y in range(256):
                # 変換後の値としてあり得ないものはスルー
                if dp[x][y] == INF:
                    pass    
                # 圧縮をすべて試す
                for c in C:
                    # 変換と丸め込み
                    next_y = round255(y + c)
                    tmp_sum = dp[x][y] + (X[x] - next_y)*(X[x] - next_y)
                    if tmp_sum <= dp[x+1][next_y]:
                        dp[x+1][next_y] = tmp_sum
        # 回答の一時記録
        res.append(min(dp[-1]))
    for i in res:
        print(i)

if __name__ == '__main__':
    main()