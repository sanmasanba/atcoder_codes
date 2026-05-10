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
    N, X = map(int, input().split(' '))
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split(' '))
        A.append(a)
        B.append(b)
    
    dp = [[0 for j in range(10010)] for i in range(N+1)]

    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(10000):
            if dp[i-1][j] == 1:
                if j + A[i-1] <= 10000:
                    dp[i][j + A[i-1]] = 1
                if j + B[i-1] <= 10000:
                    dp[i][j + B[i-1]] = 1

    print('Yes' if dp[N][X] == 1 else 'No')

if __name__ == '__main__':
    main()