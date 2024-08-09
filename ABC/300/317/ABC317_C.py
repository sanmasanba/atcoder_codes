#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

# main
N, M = map(int, input().split(' '))
G = {}
for _ in range(M):
    s, g, weight = map(int, input().split(' '))
    if s not in G:
        G[s] = {}
    G[s][g] = weight
    if g not in G:
        G[g] = {}
    G[g][s] = weight

ans = 0
seen = set()
def dfs(v:int, res:int):
    # 頂点vを探索済みにする
    global ans
    seen.add(v)    
    # 探索
    if res>ans: ans=res
    for next_v, weight in G[v].items():
        # 探索済みならスルー
        if next_v in seen:
            continue
        dfs(next_v, res+weight)
    seen.remove(v)

# すべての点から試す
for i in range(1, N+1):
    if i in G:
        dfs(i, 0)

print(ans)
