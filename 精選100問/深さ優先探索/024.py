#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')
# DFS
seen = set()
res_first = []
res_last = []
ptr = 0
def dfs(G, v):
    global ptr
    global res_first
    global res_last

    # 頂点vを探索済みにする
    seen.add(v)
    ptr += 1
    res_first[v] = ptr

    # 探索
    for next_v in G[v]:
        # 探索済みならスルー
        if next_v in seen:
            continue
        dfs(G, next_v)
    ptr += 1
    res_last[v] = ptr

#main
def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N):
        g = list(map(int, input().split(' ')))
        for i in g[2:]:
            G[g[0]-1].append(i-1)
    global res_first
    global res_last
    # 行きがけ順と帰りがけ順のリスト
    res_first = [0 for _ in range(N)]
    res_last = [0 for _ in range(N)]

    # 探索済みでない点をすべて探索
    for v in range(N):
        if v not in seen:
            dfs(G, v)
    for i in range(N):
        print(i+1, res_first[i], res_last[i])

if __name__ == '__main__':
    main()