#library
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

D = [[-1, 0], [1, 0], [0, -1], [0, 1]]

#main
def main():
    # intput
    N = int(input()) + 2
    S = ['#'*N for _ in range(N)]
    p1, p2 = None, None
    for i in range(1, N-1):
        s = '#' + input().strip() + '#'
        for j, c in enumerate(s):
            if c == 'P':
                if p1 is None: p1 = (i, j)
                else : p2 = (i, j)
        S[i] = s

    # p1とp2が遷移可能な状態をそれぞれ(p1i, p1j)(p2i, p2j)としたとき
    # (N**2)**2の盤面で表現できる
    # N**4乗の盤面は定数倍が悪い
    grid = [[INF]*(N**2) for _ in range(N**2)]
    grid[p1[0]*N+p1[1]][p2[0]*N+p2[1]] = 0

    # BFS
    que = deque([(p1[0], p1[1], p2[0], p2[1])])
    while que:
        p1i, p1j, p2i, p2j = que.popleft()

        for di, dj in D:
            np1i, np1j, np2i, np2j = p1i+di, p1j+dj, p2i+di, p2j+dj
            if S[np1i][np1j] == '#': np1i, np1j = p1i, p1j
            if S[np2i][np2j] == '#': np2i, np2j = p2i, p2j

            if np1i*N+np1j > np2i*N+np2j:
                np1i, np1j, np2i, np2j = np2i, np2j, np1i, np1j

            if grid[np1i*N+np1j][np2i*N+np2j] == INF:
                grid[np1i*N+np1j][np2i*N+np2j] = grid[p1i*N+p1j][p2i*N+p2j] + 1
                que.append((np1i, np1j, np2i, np2j))

    res = INF
    for i in range(N):
        for j in range(N):
            res = min(grid[i*N+j][i*N+j], res)
    print(-1 if res == INF else res)

if __name__ == '__main__':
    main()