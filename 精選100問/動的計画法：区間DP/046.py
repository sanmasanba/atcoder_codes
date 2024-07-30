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
    Matricses = [list(map(int, input().split(' '))) for _ in range(N)]
    
    # dpの準備
    dp = [[INF for j in range(N)] for i in range(N)]
    # 左と右の区間が一致する(行列が一つ)なら、積の数は0
    for i in range(N):
        dp[i][i] = 0

    # dp
    # 左と右の間が開いていく動きを考える
    for add in range(1, N):
        for left in range(N-add):    
            right = left + add
            # A = (a, b)、B = (b, c)の行列を考える
            # 行列ABを作るために必要な計算量はabcになる
            # ここで、行列積M_0・M_1・M_2・M_i・...・M_jを考える
            # この時、行列積は(M_0・M_1・...・M_k)*(M_(k+1)・M_(k+2)・...・M_j)
            # という、二つの行列積で表すことができる。
            # したがって、iからjまでの行列積は
            # | ・M_iからM_kまでの行列積の計算回数
            # | ・M_(k+1)からM_jまでの行列積の計算回数
            # | ・上の二つを掛け合わせたときの計算回数
            # これらの総和をもって、計算回数を求めることができる。
            # 
            # 二つの行列積を掛け合わせたときの計算回数は、最初の仮定から
            # M_i(row) * M_K(col) * M_j(col)となる
            for k in range(left, right):
                dp[left][right] = min(dp[left][right], dp[left][k] + dp[k+1][right] + Matricses[left][0]*Matricses[k][1]*Matricses[right][1])

    print(dp[0][-1])

if __name__ == '__main__':
    main()