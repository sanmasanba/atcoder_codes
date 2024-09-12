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
def check_hol(S, N, i, j):
    res = False
    if 5 < j:
        res |= sum([S[i][j-k] == '.' for k in range(1, 6)]) < 3
    if j < N - 5:
        res |= sum([S[i][j+k] == '.' for k in range(1, 6)]) < 3 
    return res

def check_ver(S, N, i, j):
    res = False
    if 5 < i:
        res |= sum([S[i-k][j] == '.' for k in range(1, 6)]) < 3
    if i < N - 5:
        res |= sum([S[i+k][j] == '.' for k in range(1, 6)]) < 3 
    return res

def check_dia(S, N, i, j):
    res = False
    # 左上
    if 5 < i and 5 < j:
        res |= sum([S[i-k][j-k] == '.' for k in range(1, 6)]) < 3
    # 右上
    if 5 < i and j < N - 5:
        res |= sum([S[i-k][j+k] == '.' for k in range(1, 6)]) < 3
    # 
    if i < N - 5 and 5 < j:
        res |= sum([S[i+k][j-k] == '.' for k in range(1, 6)]) < 3
    # 
    if i < N - 5 and j < N - 5:
        res |= sum([S[i+k][j+k] == '.' for k in range(1, 6)]) < 3
    return res

#main
def main():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(list(input()))
        
    res = False
    for i in range(N):
        for j in range(N):
            # 黒のところを基準に判定
            if S[i][j] == '#':
                res |= check_hol(S, N, i, j)
                res |= check_ver(S, N, i, j)
                res |= check_dia(S, N, i, j)

    print("Yes" if res else "No")

if __name__ == '__main__':
    main()