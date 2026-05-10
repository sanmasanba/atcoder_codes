#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')
# DFS
#BFS
def bfs(G, N1, N2, s):
    # dist:vからの距離, queue:探索キュー
    dist = [-1 for _ in range(N1+N2)]
    queue = deque()
    dist[s] = 0
    queue.append(s)
    while queue:
        v = queue.popleft()
        for next_v in G[v]:
            if dist[next_v] != -1:
                continue
            dist[next_v] = dist[v] + 1
            queue.append(next_v)
    return dist[v]

#main
def main():
    N1, N2, M = map(int, input().split(' '))
    G = [[] for _ in range(N1+N2)]
    for _ in range(M):
        a, b = map(lambda x:int(x)-1, input().split(' '))
        G[a].append(b)
        G[b].append(a)
    # 1から最も遠い点 + N1+N2から最も遠い点 + 1
    print(bfs(G, N1, N2, 0) + bfs(G, N1, N2, N1+N2-1) + 1)

if __name__ == '__main__':
    main()