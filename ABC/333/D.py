#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')
# DFS
seen = set()
def dfs(tree, v):
    # 頂点vを探索済みにする
    seen.add(v)
    d = 1
    # 探索
    for next_v in tree[v]:
        # 探索済みならスルー
        if next_v in seen:
            continue
        d += dfs(tree, next_v)
    dims[v] += d
    seen.remove(v)
    return dims[v]

#main
def main():
    # input
    N = int(input())
    tree = {i:[] for i in range(N)}
    for _ in range(N-1):
        u, v = map(lambda x:int(x)-1, input().split(' '))
        tree[u].append(v); tree[v].append(u)

    # dfsで、0から頂点を消すのに必要な連結数を求める
    global dims
    dims = [0 for _ in range(N)]
    dfs(tree, 0)
    # 元から葉のとき、1で可能
    if len(tree[0]) == 1:
        print(1)
    # 最大のもの以外は消すことで最小になる
    else:
        dims = [dims[node] for node in tree[0]]
        print(1 + sum(dims)-max(dims))

if __name__ == '__main__':
    main()