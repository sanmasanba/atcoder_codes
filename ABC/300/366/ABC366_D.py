#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations
from typing import List

sys.setrecursionlimit(10**6)
INF = float('inf')

class cumsum3d:
    """
    3次元累積和
    """
    def __init__(self, A: List[int]) -> int:
        X = len(A)
        Y = len(A[0])
        Z = len(A[0][0])
        self.cumsum = [[[0] * Z for _ in range(Y)] for _ in range(X)]
        for x in range(X):
            for y in range(Y):
                for z in range(Z):
                    self.cumsum[x][y][z] = A[x][y][z]
                    if x > 0: self.cumsum[x][y][z] += self.cumsum[x-1][y][z]
                    if y > 0: self.cumsum[x][y][z] += self.cumsum[x][y-1][z]
                    if z > 0: self.cumsum[x][y][z] += self.cumsum[x][y][z-1]
                    if x > 0 and y > 0: self.cumsum[x][y][z] -= self.cumsum[x-1][y-1][z]
                    if x > 0 and z > 0: self.cumsum[x][y][z] -= self.cumsum[x-1][y][z-1]
                    if y > 0 and z > 0: self.cumsum[x][y][z] -= self.cumsum[x][y-1][z-1]
                    if x > 0 and y > 0 and z > 0: self.cumsum[x][y][z] += self.cumsum[x-1][y-1][z-1]
    
    def get(self, lx: int, ly: int, lz: int, rx: int, ry: int, rz: int) -> int:
        """
        (lx, ly, lz)と(rx, ry, rz)で囲まれた空間の累積を求める
        """
        res = self.cumsum[rx][ry][rz]
        if lx > 0: res -= self.cumsum[lx-1][ry][rz]
        if ly > 0: res -= self.cumsum[rx][ly-1][rz]
        if lz > 0: res -= self.cumsum[rx][ry][lz-1]
        if lx > 0 and ly > 0: res += self.cumsum[lx-1][ly-1][rz]
        if lx > 0 and lz > 0: res += self.cumsum[lx-1][ry][lz-1]
        if ly > 0 and lz > 0: res += self.cumsum[rx][ly-1][lz-1]
        if lx > 0 and ly > 0 and lz > 0: res -= self.cumsum[lx-1][ly-1][lz-1]

        return res

#main
def main():
    N = int(input())
    A = [[[int(x) for x in input().split()] for _ in range(N)] for _ in range(N)]
    # 累積和の計算
    A_cumsum = cumsum3d(A)
    Q = int(input())
    LR = [list(map(lambda x: int(x)-1, input().split())) for _ in range(Q)]
    
    for lx, rx, ly, ry, lz, rz in LR:
        print(A_cumsum.get(lx, ly, lz, rx, ry, rz))

if __name__ == '__main__':
    main()