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
G = defaultdict(set)
for _ in range(N-1):
    a, b = map(lambda x:int(x)-1, input().split(' '))
    G[a].add(b)
    G[b].add(a)
V = set(map(lambda x:int(x)-1, input().split(' ')))

seen = [False] * N
ans = 0

def dfs(v):
    seen[v] = True
    res = False
    global ans
    for next_v in G[v]:
        if seen[next_v]:
            continue
        res |= dfs(next_v)
    res = v in V or res
    ans += 1 if res else 0
    return res

dfs(min(V))
print(ans)