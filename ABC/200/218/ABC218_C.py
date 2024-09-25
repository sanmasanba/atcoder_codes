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
# 一致する左上を探す
def find_left_top(L:list, N:int):
    for i in range(N):
        for j in range(N):
            if L[i][j] == '#':
                return i, j 

# オフセットを決める
def find_offset(S:list, T:list, N:int):
    si, sj = find_left_top(S, N)
    ti, tj = find_left_top(T, N)
    return ti-si, tj-sj

# 一致するかチェック
def check(S:list, T:list, N:int):
    dh, dw = find_offset(S, T, N)
    for i in range(N):
        for j in range(N):
            ti, tj = i+dh, j+dw
            if 0 <= ti < N and 0 <= tj < N:     
                if S[i][j] != T[ti][tj]: return False
            else:
                if S[i][j] == '#': return False
    return True

# 回転
def rotate(T: list):
    return list(zip(*T[::-1]))

#main
def main():
    # input
    N = int(input())
    S, T = [], []
    for _ in range(N):
        S.append(list(input()))
    for _ in range(N):
        T.append(list(input()))

    # '#'の数が不一致のとき、一致しない
    cntS = sum(1 for i in range(N) for j in range(N) if S[i][j]=='#')
    cntT = sum(1 for i in range(N) for j in range(N) if T[i][j]=='#')
    if cntS != cntT:
        print('No')
        sys.exit(0)

    res = False
    for _ in range(4):
        # rotate
        T = rotate(T)
        res |= check(S, T, N)
    print("Yes" if res else "No") 

if __name__ == '__main__':
    main()