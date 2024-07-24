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
    N, W = map(int, input().split(' '))
    Weight_Value = []
    for _ in range(N):
        v, w = map(int, input().split(' '))
        Weight_Value.append([w, v])

    # dpの準備
    dp = [[0 for j in range(W+1)] for i in range(N+1)]
    for nums in range(1, 1+N):
        weight, value = Weight_Value[nums-1]
        for up_to_weight in range(1, W+1):
            # 更新の可能性がある場合は比較
            if up_to_weight - Weight_Value[nums-1][0] >= 0:
                # 選ばなかったときと選んだ時で価値を比較
                dp[nums][up_to_weight] = max(dp[nums-1][up_to_weight - weight]+value, dp[nums-1][up_to_weight])
            # 更新の可能性がない場合はそのまま
            else:
                dp[nums][up_to_weight] = dp[nums-1][up_to_weight]
    print(dp[N][W])

if __name__ == '__main__':
    main()