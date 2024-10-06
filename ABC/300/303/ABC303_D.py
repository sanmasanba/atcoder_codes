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
    X, Y, Z = map(int, input().split(' '))
    S = list(input())
    N = len(S)

    # on, offでdpを遷移
    dp = [[0, 0] for _ in range(N+1)]
    # あらかじめ、capslockを押しておく
    dp[0][1] = Z

    for i in range(N):
        s = S[i]
        # 小文字
        if s == 'a':
            dp[i+1][0] = min(dp[i][0]+X, dp[i][1]+Z+X)
            dp[i+1][1] = min(dp[i][1]+Y, dp[i][0]+Z+Y)
        # 大文字
        else:
            dp[i+1][0] = min(dp[i][1]+Z+Y, dp[i][0]+Y)
            dp[i+1][1] = min(dp[i][0]+Z+X, dp[i][1]+X)
    
    print(min(dp[-1]))

if __name__ == '__main__':
    main()