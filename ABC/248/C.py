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
    N, M, K = map(int, input().split(' '))
    
    # dp[i][sum] := 数列のi番目まで確定していて、総和がsumになる組み合わせ
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    # 0は何もなくても達成できるので1
    dp[0][0] = 1

    # n番目までで
    for i in range(N):
        # m-1番目までの総和k
        for k in range(K):
            # m番目の値
            for m in range(1, M+1):
                if k+m <= K: dp[i+1][k+m] += dp[i][k]
    
    res = 0
    for i in range(1, K+1):
        res += dp[-1][i]
    print(res%MOD)

if __name__ == '__main__':
    main()