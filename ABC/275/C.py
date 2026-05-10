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
seen = set()
def check(S, r, c, i, j):
    x2 = j; y2 = r+i
    if 9 <= x2 or  9 <= y2 or S[y2][x2] != '#':
        return False
    j -= c
    x3 = c+i+j; y3 = r+i-j
    x4 = c+i; y4 = r-j
    dots = [(c, r), (x2, y2), (x3, y3), (x4, y4)]
    dots = tuple(sorted(dots))
    if not 0 <= x3 < 9 or not 0 <= y3 < 9 or not 0 <= x4 < 9 or not 0 <= y4 < 9:
        return False
    if S[y3][x3] == '#' and S[y4][x4] == '#' and dots not in seen:
        seen.add(dots)
        return True
    else:
        return False

#main
def main():
    S = []
    for _ in range(9):
        S.append(list(input()))
    
    # 全探索
    res = 0
    for r in range(9):
        for c in range(9):
            if S[r][c] == '#':
                for i in range(1, 9):
                    if 9 <= r+i:
                        break
                    for j in range(9):
                        if check(S, r, c, i, j):
                            res += 1
    print(res)

if __name__ == '__main__':
    main()