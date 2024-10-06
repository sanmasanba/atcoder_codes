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
#BFS
def bfs(G, s):
    visited[s] = True
    queue = deque()
    queue.append(s)
    nodes, edges = 1, 0
    while queue:
        v = queue.popleft()
        for next_v in G[v]:
            edges += 1
            if visited[next_v]:
                continue
            visited[next_v] = True
            nodes += 1
            queue.append(next_v)
    return nodes, edges//2

#main
def main():
    # input
    N, M = map(int, input().split(' '))
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x:int(x)-1, input().split(' '))
        G[a].append(b)
        G[b].append(a)
    
    global visited
    visited = [False] * N

    res = 0
    for i in range(N):
        # 独立したグラフごとに、接続可能な頂点数からすでにある辺の数を引く
        if not visited[i]:
            nodes, edges = bfs(G, i)
            res += (nodes*(nodes-1))//2 - edges
    print(res) 

if __name__ == '__main__':
    main()