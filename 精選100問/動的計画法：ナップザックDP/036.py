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
    items = []
    for _ in range(N):
        v, w = map(int, input().split(' '))
        items.append([w, v])
    # ソートする
    items.sort()
    
    # dpの準備
    dp = [0 for j in range(W+1)]
    # 上限ごとに
    for up_to_weight in range(1, W+1):
        for weight, value in items:
            # 残りの荷物が上限を超えるとき、ブレーク
            if weight > up_to_weight:
                break
            # 今の値と更新後の比較
            dp[up_to_weight] = max(dp[up_to_weight], dp[up_to_weight-weight]+value)

    print(dp[-1])

if __name__ == '__main__':
    main()