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

# 考察
# この手の問題は二分探索
# 訓練回数を二分探索する
# ノード間の移動はbfsでやる
# -> O(探索範囲 * 開始ノード数 * 訪問するノード数 * ノードから延びるエッジ数)
# -> O(N^3 * logP)

def manhattan_distance(x1: T, x2: T, y1: T, y2: T) -> T:
    return abs(x2-x1) + abs(y2-y1)

# main
def main():
    # intput
    N = int(input())
    x, y, p = zip(*[list(map(int, input().split())) for _ in range(N)])

    dist = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j: 
                continue
            tmp = manhattan_distance(x[i], x[j], y[i], y[j])
            dist[i][j] = tmp
            dist[j][i] = tmp

    def bfs(s, ans):
        seen = set()
        seen.add(s)
        q = deque([s])
        while q:
            cur = q.popleft()
            for nxt in range(N):
                if nxt not in seen and dist[cur][nxt] <= ans * p[cur]:
                    seen.add(nxt)
                    q.append(nxt)
        return len(seen) == N

    res = 1 << 64
    for s in range(N):
        ok = res
        ng = 0
        if not bfs(s, ok):
            continue
        while ok-ng > 1:
            mi = (ok + ng) // 2
            if bfs(s, mi):
                ok = mi
            else:
                ng = mi
        res = min(res, ok)
    print(res)

if __name__ == '__main__':
    main()
