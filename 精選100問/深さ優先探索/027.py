#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations, product

sys.setrecursionlimit(10**6)
INF = float('inf')

# DFS
def dfs(G, v, seen):
    # 頂点vを探索済みにする
    seen.add(v)
    res = 0
    for next_v in G[v]:
        # 探索(探索済みならスルー)
        if next_v not in seen:
            tmp = dfs(G, next_v, seen)
            res = max(res,tmp)
    # ほかの経路から、探索可能にするために消す
    seen.remove(v)
    return 1 + res

#main
def main():
    M = int(input())
    N = int(input())
    G = [[] for _ in range(N*M)]
    MAP = [list(map(int, input().split(' '))) for _ in range(N)]
    for i in range(N*M):
            H = i//M
            W = i%M
            for j, k in [[0 ,-1], [-1, 0], [0, 1], [1, 0]]:
                if 0 <= H+j < N and 0 <= W+k < M and MAP[H][W] == 1 and MAP[H+j][W+k] == 1:
                    G[i].append(M*(H+j) + W+k)

    res = 0
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 1:
                if len(G[i*N + j])  == 0:
                    res = max(res, 1)
                else:
                    seen = set()
                    res = max(res, dfs(G, i*N + j, seen))
    print(res)

if __name__ == '__main__':
    main()