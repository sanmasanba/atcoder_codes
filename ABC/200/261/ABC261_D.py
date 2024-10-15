#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    # input
    N, M = map(int, input().split(' '))
    X = list(map(int, input().split(' ')))
    bonuses = [0] * 5001
    for _ in range(M):
        c, y = map(int, input().split(' '))
        bonuses[c] = y

    # dp[n][m]:=nターンに、カウントがmとなるときの最大値
    dp = [[0] * 5001 for _ in range(5001)]
    for turn in range(1, N+1):
        # 表の更新
        for count in range(1, turn+1):
            # nターンにカウントがmとなるとき、n-1ターンでは、カウントはm-1である
            dp[turn][count] = dp[turn-1][count-1] + X[turn-1] + bonuses[count]

        # 裏の更新
        dp[turn][0] = 0
        dp[turn][0] = max(dp[turn][0], max(dp[turn-1]))

    # output
    print(max(dp[N]))

if __name__ == '__main__':
    main()