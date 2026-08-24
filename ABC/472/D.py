# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, NamedTuple, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

def cumsum2d(a:List[T]) -> List[T]:
    h, w = len(a), len(a[0])
    tmp = [[0] * (w+1) for _ in range(h+1)]
    for i in range(h):
        for j in range(w):
            tmp[i+1][j+1] = (
                tmp[i+1][j]
                + tmp[i][j+1]
                - tmp[i][j]
                + a[i][j]
                )
    return tmp

# main
def main():
    # intput
    H, W, K = map(int, input().split())
    S = [list(input().strip()) for _ in range(H)]

    # 危険なマスを取り除く
    hs, ws = set(i for i in range(H)), set(i for i in range(W))
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                hs.discard(i)
                ws.discard(j)

    # 安全マスをメモ
    dist = [[INF]*W for _ in range(H)]
    q = deque()
    for i in range(H):
        for j in range(W):
            if i in hs and j in ws:
                q.append((i, j))
                dist[i][j] = 0

    # 多始点BSFでK未満を探す
    # 文字列の指定がないときはmove2dを消す
    dij = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while q:
        si, sj = q.popleft()
        if K <= dist[si][sj]:
            continue
        for di, dj in dij:
            ni, nj = si+di, sj+dj
            if not (0 <= ni < H and 0 <= nj < W):
                continue
            if S[ni][nj] == '#' or dist[ni][nj] != INF:
                continue
            dist[ni][nj] = dist[si][sj] + 1
            q.append((ni, nj))

    res = 0
    for i in range(H):
        for j in range(W):
            if dist[i][j] <= K:
                res += 1
    print(res)

if __name__ == '__main__':
    main()
