#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

# 累積和を計算する関数
def compute_cumsum(A, N):
    A_cumsum = [[[0] * N for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            for z in range(N):
                A_cumsum[x][y][z] = A[x][y][z]
                if x > 0:
                    A_cumsum[x][y][z] += A_cumsum[x-1][y][z]
                if y > 0:
                    A_cumsum[x][y][z] += A_cumsum[x][y-1][z]
                if z > 0:
                    A_cumsum[x][y][z] += A_cumsum[x][y][z-1]
                if x > 0 and y > 0:
                    A_cumsum[x][y][z] -= A_cumsum[x-1][y-1][z]
                if x > 0 and z > 0:
                    A_cumsum[x][y][z] -= A_cumsum[x-1][y][z-1]
                if y > 0 and z > 0:
                    A_cumsum[x][y][z] -= A_cumsum[x][y-1][z-1]
                if x > 0 and y > 0 and z > 0:
                    A_cumsum[x][y][z] += A_cumsum[x-1][y-1][z-1]
    return A_cumsum

#main
def main():
    N = int(input())
    A = [[[int(x) for x in input().split()] for _ in range(N)] for _ in range(N)]
    # 累積和の計算
    A_cumsum = compute_cumsum(A, N)
    Q = int(input())
    LR = [list(map(lambda x: int(x)-1, input().split())) for _ in range(Q)]
    
    for lx, rx, ly, ry, lz, rz in LR:
        # [0, 0, 0]からの体積を求める
        total = A_cumsum[rx][ry][rz]
        # いらない部分を引いていく
        if lx > 0:
            total -= A_cumsum[lx-1][ry][rz]
        if ly > 0:
            total -= A_cumsum[rx][ly-1][rz]
        if lz > 0:
            total -= A_cumsum[rx][ry][lz-1]
        # 重複したところを戻す
        if lx > 0 and ly > 0:
            total += A_cumsum[lx-1][ly-1][rz]
        if lx > 0 and lz > 0:
            total += A_cumsum[lx-1][ry][lz-1]
        if ly > 0 and lz > 0:
            total += A_cumsum[rx][ly-1][lz-1]
        if lx > 0 and ly > 0 and lz > 0:
            total -= A_cumsum[lx-1][ly-1][lz-1]
        print(total)

if __name__ == '__main__':
    main()