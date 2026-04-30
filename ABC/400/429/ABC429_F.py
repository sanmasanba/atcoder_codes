# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial, isqrt
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
D = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def _input(N, sqrtN):
    S = list(input().strip())
    tmp = []
    i = 0
    while i*sqrtN < N:
        tmp.append(S[i*sqrtN:min(N, (i+1)*sqrtN)])
        i += 1
    return tmp

def is_out_of_range(x:int, y:int, Xmi:int, Xma:int, Ymi:int, Yma:int) -> bool:
    return not (Xmi <= x < Xma and Ymi <= y < Yma)

# BFS
def bfs(G, s):
    if G[s][0] == '#':
        return [-1, -1, -1]
    dist = [[-1]*len(G[0]) for _ in range(3)]
    queue = deque()
    dist[s][0] = 0
    queue.append([s, 0])
    while queue:
        x, y = queue.popleft()
        for dx, dy in D:
            nx, ny = x+dx, y+dy
            if (is_out_of_range(nx, ny, 0, 3, 0, len(G[0]))
                or dist[nx][ny] != -1 
                or G[nx][ny] == '#'):
                continue
            dist[nx][ny] = dist[x][y] + 1
            queue.append([nx, ny])
    return [dist[0][-1], dist[1][-1], dist[2][-1]]

# main
def main():
    # intput
    N = int(input())
    sqrtN = isqrt(N)
    tmp0 = _input(N, sqrtN)
    tmp1 = _input(N, sqrtN)
    tmp2 = _input(N, sqrtN)
    MAP = [[i, j, k] for i, j, k in zip(tmp0, tmp1, tmp2)]
    pos = []
    tmp = 0
    for m in tmp0:
        tmp += len(m)
        pos.append(tmp)
    dist = [[[0]*3 for _ in range(3)] for _ in range(len(MAP))]
    def update(i, m):
        for s in range(3):
            tmp = bfs(m, s)
            dist[i][s] = tmp
    for i, m in enumerate(MAP):
        update(i, m)
    
    Q = int(input())
    for _ in range(Q):
        r, c = map(int, input().split())
        p = bisect_left(pos, c)
        r, c = r-1, c-1
        if MAP[p][r][c-pos[p]] == "#": MAP[p][r][c-pos[p]] = "."  
        else: MAP[p][r][c-pos[p]] = "#"
        update(p, MAP[p])
        dp = [[INF]*3 for _ in range(len(dist)+1)]
        dp[0][0] = -1
        for i in range(len(dist)):
            for j in range(3):
                if (dp[i][j] == INF 
                    or MAP[i][j][0] == '#'): continue
                for k in range(3):
                    if dist[i][j][k] == -1: continue
                    dp[i+1][k] = min(dp[i+1][k], dp[i][j] + dist[i][j][k] + 1)
        print(-1 if dp[-1][-1] == INF else dp[-1][-1])

if __name__ == '__main__':
    main()