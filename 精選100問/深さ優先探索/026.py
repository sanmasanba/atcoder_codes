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
def dfs(G, v, parent, res):
    # 探索
    for next_v in G[v]:
        # 探索済みならスルー
        if next_v == parent:
            continue
        res[next_v] += res[v]
        dfs(G, next_v, v, res)

#main
def main():
    N, Q = map(int, input().split(' '))
    tree = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split(' '))
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)
    PX = []
    for _ in range(Q):
        p, x = map(int, input().split(' '))
        PX.append([p-1, x])

    # 部分木の根の部分に累積値を追加
    res = [0 for _ in range(N)]
    for p, x in PX:
        res[p] += x
    dfs(tree, 0, -1, res)
    print(*res)

if __name__ == '__main__':
    main()