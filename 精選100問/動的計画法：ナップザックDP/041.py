#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    D, N = map(int, input().split(' '))
    thermals = [int(input()) for _ in range(D)]
    clothes = [list(map(int, input().split(' '))) for _ in range(N)]
    
    # DPの準備
    dp = [[-1]*D for _ in range(N)]
    # 初日は、条件にはまっているすべての日を[派手さ, 0]にする)
    for i, cloth in enumerate(clothes):
        low, high, _ = cloth
        if low <= thermals[0] <= high:
            dp[i][0] = 0
    # DP
    # 今日の服と昨日の服で考える
    for day, thermal in enumerate(thermals[1:], start=1):
        # 服iが条件にはまっているかを比較
        for today_cloth, today in enumerate(clothes):
            low, high, today_c = today
            # 条件の時、更新
            if low <= thermal <= high:
                # 昨日選んだ服の派手さの総和の最大値と比較
                for pre_cloth, pre in enumerate(clothes):
                    _, _, pre_c = pre
                    # 昨日着た服の分だけ比較し、派手さの最大値が更新されるなら更新
                    if dp[pre_cloth][day-1] != -1 and dp[today_cloth][day] <= dp[pre_cloth][day-1] + abs(today_c - pre_c):
                        dp[today_cloth][day] = dp[pre_cloth][day-1] + abs(today_c - pre_c)
    # 出力
    res = 0
    for i in range(N):
        res = max(res, dp[i][-1])
    print(res)


if __name__ == '__main__':
    main()