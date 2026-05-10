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
    N, A, B = map(int, input().split(' '))
    P, Q, R, S = map(int, input().split(' '))

    # 一つ目の操作
    L1 = max(1-A, 1-B)
    R1 = min(N-A, N-B)
    # 二つ目の操作
    L2 = max(1-A, B-N)
    R2 = min(N-A, B-1)

    for i in range(Q-P+1):
        # Pマス目を基準とする(1-indexed)
        h = P+i
        for j in range(S-R+1):
            # Rマス目を基準とする(1-indexed)
            w = R+j

            # 判定する
            # 条件は縦h、横wとしたとき、変形により
            # 条件１：max(1-A, 1-B) <= h-A <= min(N-A, N-B) and max(1-A, 1-B) <= w-B <= min(N-A, N-B)
            # 条件２：max(1-A, B-N) <= h-A <= min(N-A, B-1) and max(1-A, B-N) <= B-w <= min(N-A, B-1)
            # となるので、どちらかに該当しているなら#を書けばよい(計算量はO(1))
            if h-A == w-B and (L1 <= h-A <= R1 and L1 <= w-B <= R1):
                print("#", end='')
            elif h-A == B-w and (L2 <= h-A <= R2 and L2 <= B-w <= R2):
                print("#", end='')
            else:
                print(".", end='')
        print()

if __name__ == '__main__':
    main()