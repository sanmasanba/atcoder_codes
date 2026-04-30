# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

# main
def main():
    # intput
    H, W = map(int, input().split())

    A = [[[0]*(W+2) for _ in range(H+2)] for _ in range(2)]
    S, G = None, None
    for i in range(H):
        s = list(input().strip())
        for j, a in enumerate(s):
            if a == '.':
                A[0][i+1][j+1] = 1
                A[1][i+1][j+1] = 1
            elif a == 'S':
                S = (0, i+1, j+1)
                A[0][i+1][j+1] = 1
                A[1][i+1][j+1] = 1
            elif a == 'G':
                G = (i+1, j+1)
                A[0][i+1][j+1] = 1
                A[1][i+1][j+1] = 1
            elif a == 'o':
                A[0][i+1][j+1] = 1
            elif a == 'x':
                A[1][i+1][j+1] = 1
            elif a == '?':
                A[0][i+1][j+1] = 2
                A[1][i+1][j+1] = 2

    # BFS
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    def bfs(S):
        # dist:vからの距離, queue:探索キュー
        dist = [[[INF]*(W+2) for _ in range(H+2)] for _ in range(2)]
        queue = deque()
        dist[S[0]][S[1]][S[2]] = 0
        queue.append(S)
        
        while queue:
            x, y, z = queue.popleft()
            for dy, dz in d:
                nx, ny, nz = x, y+dy, z+dz
                if not A[nx][ny][nz]: continue
                nx = (x + A[nx][ny][nz]==2)%2
                if dist[nx][ny][nz] != INF: continue
                dist[nx][ny][nz] = dist[x][y][z] + 1
                queue.append((nx, ny, nz))
        return dist
    
    dist = bfs(S)
    res = min(dist[0][G[0]][G[1]], dist[1][G[0]][G[1]])
    print(-1 if res == INF else res)

if __name__ == '__main__':
    main()