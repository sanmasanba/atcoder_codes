#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
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
            dist[next_v] = dist[v] + 1
            queue.append(next_v)
    return dist

#main
def main():
    N = int(input())
    G = [None for _ in range(N)]
    for _ in range(N):
        v, k, *to = map(lambda x: int(x)-1, input().split(' '))
        G[v] = (to)
    
    res = bfs(G, N, 0)
    for i in range(N):
        print(i+1, res[i])

if __name__ == '__main__':
    main()