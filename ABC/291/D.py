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
    A, B = [], []
    duplicates = set()
    for i in range(N):
        a, b = map(int, input().split(' '))
        A.append(a)
        B.append(b)
    
    # dp[0]:表, dp[1]:裏
    dp = [1, 1]

    for i in range(1, N):
        # 今の札と前の札を比べる
        front_front = 0 if (A[i-1] == A[i]) else dp[0]
        back_front = 0 if (B[i-1] == A[i]) else dp[1]
        front_back = 0 if (A[i-1] == B[i]) else dp[0]
        back_back = 0 if (B[i-1] == B[i]) else dp[1]

        dp = [(front_front+back_front)%MOD, (front_back+back_back)%MOD]
    
    print(sum(dp)%MOD)

if __name__ == '__main__':
    main()