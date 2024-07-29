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
    N = int(input())
    S = [list(input()) for _ in range(5)]

    c2i = {"R":0, "B":1, "W":2}
    dp = [[INF]*3 for _ in range(N)]
    # 初期化
    for k in ["R", "B", "W"]:
        dp[0][c2i[k]] = 5 - sum(S[row][0] == k for row in range(5))
    
    for col in range(1, N):
        tmp_col = ''
        for row in range(5):
            tmp_col += S[row][col]
        C = Counter(tmp_col)
        for k in ["R", "B", "W"]:
            if k in C:
                v = 5 - C[k]
                tmp_k1 = (c2i[k]+1)%3
                tmp_k2 = (c2i[k]+2)%3
                dp[col][c2i[k]] = min(dp[col-1][tmp_k1]+v, dp[col-1][tmp_k2]+v)
            else:
                tmp_k1 = (c2i[k]+1)%3
                tmp_k2 = (c2i[k]+2)%3
                dp[col][c2i[k]] = min(dp[col-1][tmp_k1]+5, dp[col-1][tmp_k2]+5)

    print(min(dp[-1]))

if __name__ == '__main__':
    main()