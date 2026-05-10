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
def bfs(G, N, s):
    # dist:vからの距離, queue:探索キュー
    dist = [-1 for _ in range(N)]
    queue = deque()
    dist[s] = 0
    queue.append(s)
    while queue:
        v = queue.popleft()
        for next_v in G[v]:
            if dist[next_v] != -1:
                continue
            dist[next_v] = (dist[v] + 1)%2
            queue.append(next_v)

    return dist

#main
def main():
    # input
    N, Q = map(int, input().split(' '))
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(lambda x: int(x)-1, input().split(' '))
        G[a].append(b)
        G[b].append(a)
    QUERY = []
    for _ in range(Q):
        c, d = map(lambda x: int(x)-1, input().split(' '))
        QUERY.append([c, d])
    
    # 二部グラフに塗分け
    dist = bfs(G, N, 0)

    # output
    for c, d in QUERY:
        c_dist = dist[c]
        d_dist = dist[d]
        if c_dist == d_dist:
            print('Town')
        else:
            print('Road')

if __name__ == '__main__':
    main()