#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N = int(input())
    XY = [list(map(int, input().split(' '))) for _ in range(N)]
    # dpで管理
    dp = [[0, 0] for _ in range(N+1)]
    # シミュレート
    for i in range(N):
        x, y = XY[i]
        if x:   # 毒入り
            dp[i+1][0] = dp[i][0]   # 健康に遷移
            dp[i+1][1] = max(dp[i][0]+y, dp[i][1])  # 不健康に遷移
        else:   # 解毒剤入り
            dp[i+1][0] = max(dp[i][0], dp[i][0]+y, dp[i][1]+y)  # 健康に遷移
            dp[i+1][1] = dp[i][1]   # 不健康に遷移
    print(max(dp[N]))   # 最終日の最大値を求める

if __name__ == '__main__':
    main()