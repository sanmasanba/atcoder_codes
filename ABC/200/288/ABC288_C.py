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
res = 0

def dfs(G, v):
    global res
    # 頂点vを探索済みにする
    seen.add(v)
    # 探索
    for next_v in G[v]:
        # 探索済みならスルー
        if next_v in seen:
            continue
        dfs(G, next_v)
        res += 1

def main():
    N, M = map(int, input().split(' '))
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split(' '))
        G[a].append(b)
        G[b].append(a)

    for i in range(N):
        if i not in seen:
            dfs(G, i)
    print(M - res)

if __name__ == "__main__":
    main()