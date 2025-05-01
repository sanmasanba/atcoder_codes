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
    A = list(map(int, input().split(' ')))
    
    res = 0
    # bitは独立で考える
    for shift in range(30):
        base = 1 << shift
        # memo := bitのそれぞれ(1 or 0)の登場数
        memo = [0, 0]
        memo[A[0] >> shift & 1] = 1
        for i in range(1, N):
            # A[i] >> shift == 1なら、0の分だけ足す
            # A[i] >> shift == 0なら、1の分だけ足す
            res += memo[~(A[i] >> shift & 1)] * base
            # 1のとき、0と1が反転する
            if A[i] >> shift & 1:
                memo = [memo[1], memo[0]]
            # i番めの項を追加
            memo[A[i] >> shift & 1] += 1
    print(res)

if __name__ == '__main__':
    main()