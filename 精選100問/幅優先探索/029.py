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
def bfs(MAP, R, C, s, g):
    # dist:vからの距離, queue:探索キュー
    dist = [[-1 for _ in range(C)] for i in range(R)]
    queue = deque()
    dist[s[0]][s[1]] = 0
    queue.append(s)
    while queue:
        v = queue.popleft()
        for next in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            if dist[v[0]+next[0]][v[1]+next[1]] != -1 or MAP[v[0]+next[0]][v[1]+next[1]] == "#":
                continue
            dist[v[0]+next[0]][v[1]+next[1]] = dist[v[0]][v[1]] + 1
            queue.append((v[0]+next[0], v[1]+next[1]))
    return dist[g[0]][g[1]]

#main
def main():
    R, C = map(int, input().split(' '))
    S = tuple(map(lambda x: int(x)-1, input().split(' ')))
    G = tuple(map(lambda x: int(x)-1, input().split(' ')))
    MAP = [list(input()) for _ in range(R)]
    
    print(bfs(MAP, R, C, S, G))

if __name__ == '__main__':
    main()