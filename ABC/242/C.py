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
MOD = 998244353

#main
def main():
    N = int(input())    
    # dp[i][j] := i桁めをjとしたときに達成可能な組み合わせ
    dp = [[0 for _ in range(9)] for _ in range(N)]
    dp[0] = [1]*9

    for i in range(N-1):
        for j in range(9):
            if j == 0:
                dp[i+1][j] = (dp[i][0]+dp[i][1])%MOD
            elif 0 < j < 8:
                dp[i+1][j] = (dp[i][j-1]+dp[i][j]+dp[i][j+1])%MOD
            else:
                dp[i+1][j] = (dp[i][7]+dp[i][8])%MOD

    print(sum(dp[-1])%MOD)

if __name__ == '__main__':
    main()