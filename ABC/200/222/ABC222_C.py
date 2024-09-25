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
def solve(p1, p2):
    if p1 == p2:
        return 0, 0
    elif (p1 == 'G' and p2 == 'C') or (p1 == 'C' and p2 == 'P') or (p1 == 'P' and p2 == 'G'):
        return 1, 0
    else:
        return 0, 1

#main
def main():
    # 入力
    N, M = map(int, input().split(' '))
    A = []
    for _ in range(2*N):
        A.append(list(input()))

    res = [[0, i] for i in range(2*N)]
    for m in range(M):
        for n in range(N):
            # 対戦者の決定
            p1 = res[2*n][1]
            p2 = res[2*n+1][1]
            # じゃんけん
            p1_res, p2_res = solve(A[p1][m], A[p2][m])
            res[2*n][0] += p1_res
            res[2*n+1][0] += p2_res
        res.sort(key=lambda x: (-x[0], x[1]))
    
    # 出力
    for p in res:
        print(p[1]+1)

if __name__ == '__main__':
    main()