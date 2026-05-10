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
    # input
    N = int(input())
    A = list(map(int, input().split(' ')))

    # dp
    dp = [[0 for _ in range(10)] for _ in range(N)]
    dp[0][A[0]] = 1
    for i in range(1, N):
        y = A[i]
        for x, cnt in enumerate(dp[i-1]):
            F = (x + y) % 10
            G = (x * y) % 10
            dp[i][F] = (dp[i][F] + cnt) % MOD
            dp[i][G] = (dp[i][G] + cnt) % MOD

    # output
    print(*dp[-1], sep='\n')

if __name__ == '__main__':
    main()