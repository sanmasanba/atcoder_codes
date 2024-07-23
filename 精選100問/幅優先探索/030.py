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
def bfs(MAP, H, W, s, g):
    # dist:vからの距離, queue:探索キュー
    dist = [[-1 for _ in range(W)] for i in range(H)]
    queue = deque()
    dist[s[0]][s[1]] = 0
    queue.append(s)
    while queue:
        v = queue.popleft()
        for next in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            if not 0 <= v[0]+next[0] < H or not 0 <= v[1]+next[1] < W or dist[v[0]+next[0]][v[1]+next[1]] != -1 or MAP[v[0]+next[0]][v[1]+next[1]] == "X":
                continue
            dist[v[0]+next[0]][v[1]+next[1]] = dist[v[0]][v[1]] + 1
            queue.append((v[0]+next[0], v[1]+next[1]))
    return dist[g[0]][g[1]]

#main
def main():
    H, W, N = map(int, input().split(' '))
    MAP = [list(input()) for _ in range(H)]
    
    check = list()
    for i in range(H):
        for j in range(W):
            if MAP[i][j] != "." and MAP[i][j] != "X":
                check.append([MAP[i][j], i, j])
    check.sort()
    tmp = check.pop()
    check = [tmp] + check

    res = 0
    for i in range(N):
        res += bfs(MAP, H, W, [check[i][1], check[i][2]], [check[i+1][1], check[i+1][2]])
    print(res)

if __name__ == '__main__':
    main()