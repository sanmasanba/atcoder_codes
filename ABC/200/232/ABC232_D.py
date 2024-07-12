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
    H, W = map(int, input().split(' '))
    C = [list(input()) for _ in range(H)]
    
    dp = [[0 for w in range(W+1)] for h in range(H+1)]
    res = 0
    dp[1][1] = 1
    flg = 0

    for h in range(H):
        for w in range(W):
            if C[h][w] == '.':
                if h == 0 and w > 0:
                    dp[h+1][w+1] = 0 if flg == 1 or C[h][w-1] == '#' else dp[h+1][w]+1
                if h > 0:
                    tmp = max(dp[h+1][w], dp[h][w+1])
                    dp[h+1][w+1] = tmp+1 if tmp else 0 
            else:
                flg = 1
                dp[h+1][w+1] = 0
            res = dp[h+1][w+1] if res < dp[h+1][w+1] else res

    print(res)

if __name__ == '__main__':
    main()