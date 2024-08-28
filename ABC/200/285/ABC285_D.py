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

N = int(input())
G = {}
not_parents = set()
name_list = []
for _ in range(N):
    s, t = input().split(' ')
    name_list.append(s)
    name_list.append(t)
    G[s] = t
res = True 
loop = {name: None for name in name_list}

# DFS
seen = set()
def dfs(G, v):
    res = True
    seen.add(v)
    # 次のノードがないならループじゃない
    if v not in G:
        return True
    # 探索済みならそのノードまでの結果を返す
    if loop[G[v]] != None:
        return loop[G[v]]
    # ループになっていたらFalse
    if G[v] in seen:
        loop[v] = False
        return loop[v]
    
    res &= dfs(G, G[v])
    loop[v] = res
    return loop[v]

for name in name_list:
    if loop[name] == None:
        loop[name] = dfs(G, name)
    res &= loop[name]
    
print("Yes" if res else "No")