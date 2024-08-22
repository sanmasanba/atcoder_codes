#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**9)
INF = float('inf')

# 深さ優先探索は、メモリ周りを意識する
seen = set()
res = {}
ans = []
N, X, Y = map(int, input().split(' '))
X -= 1
Y -= 1
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(lambda x:int(x)-1, input().split(' '))
    G[a].append(b)
    G[b].append(a)

# 再帰が深いときは、Cpythonが有効
def dfs(v):
    # 頂点vを探索済みにする
    seen.add(v)
    # 探索
    for next_v in G[v]:
        # 探索済みならスルー
        if next_v in seen:
            continue
        dfs(next_v)
        res[next_v] = v
    seen.remove(v)

dfs(X)
pos = Y
while pos != X:
    ans.append(pos+1)
    pos = res[pos]
ans.append(pos+1)
print(*reversed(ans), sep=' ')
