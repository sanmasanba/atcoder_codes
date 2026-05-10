#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    N, S, M, L = map(int, input().split(' '))
    dp = [INF for _ in range(110)]

    dp[1] = min(S, M ,L)
    for i in range(1, 101):
        if 1<= i < 13:
            if 1 <= i <= 6:
                dp[i] = min(S, M, L)
            if 7 <= i <= 8:
                dp[i] = min(dp[i-6]+S, M, L)
            if 9 <= i <= 12:
                dp[i] = min(dp[i-6]+S, dp[i-8]+M, L)
        else:
            dp[i] = min(dp[i-6]+S, dp[i-8]+M, dp[i-12]+L)

    print(dp[N])

if __name__ == '__main__':
    main()