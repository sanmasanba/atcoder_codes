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
# DFS

N, K = map(int, input().split(' '))
G = {i:set() for i in range(1, N+1)}
for _ in range(N-1):
    a, b = map(int, input().split(' '))
    if a > b:
        a, b = b, a
    G[a].add(b)
V = set(map(int, input().split(' ')))

def dfs(G, v):
    child_set = set([v])
    # 探索
    for next_v in G[v]:
        if next_v in G:
            child_set |= dfs(G, next_v)
    # print(v, child_set)
    if child_set.isdisjoint(V):
        # print(f"remove {v}")
        G.pop(v)
    return child_set

for v in V:
    dfs(G, v)

print(len(G))