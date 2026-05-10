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
    N, K = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    
    # 前の項までで満たす組合わせがあるか
    dp = [[False, False] for _ in range(N)]
    dp[0] = [True, True]

    # 最後まで組み合わせが存在すればok
    for i in range(N-1):
        dp[i+1][0] = (dp[i][0] and abs(A[i]-A[i+1]) <= K) or (dp[i][1] and abs(B[i]-A[i+1]) <= K)
        dp[i+1][1] = (dp[i][0] and abs(A[i]-B[i+1]) <= K) or (dp[i][1] and abs(B[i]-B[i+1]) <= K)

    print("Yes" if any(dp[-1]) else "No")

if __name__ == '__main__':
    main()