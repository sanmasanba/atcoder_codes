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
MOD998244353 = 998244353
MOD1000000007 = 1000000007

#BFS
def bfs(G, N, s):
    # dist:vからの距離, queue:探索キュー
    dist = [-1 for _ in range(N)]
    queue = deque()
    dist[s] = 0
    max_dist_pos = 0
    queue.append(s)
    while queue:
        v = queue.popleft()
        for next_v in G[v]:
            if dist[next_v] != -1:
                continue
            dist[next_v] = dist[v] + 1
            if dist[max_dist_pos] < dist[next_v]:
                max_dist_pos = next_v
            queue.append(next_v)
    return dist, max_dist_pos

#main
def main():
    # intput
    N1 = int(input())
    G1 = [[] for _ in range(N1)]
    for _ in range(N1-1):
        a, b = map(lambda x: int(x)-1, input().split())
        G1[a].append(b)
        G1[b].append(a)
    N2 = int(input())
    G2 = [[] for _ in range(N2)]
    for _ in range(N2-1):
        a, b = map(lambda x: int(x)-1, input().split())
        G2[a].append(b)
        G2[b].append(a)
    
    # Tree diameter
    # G1
    _, pos1 = bfs(G1, N1, 0)
    dist_from_p1, pos2 = bfs(G1, N1, pos1)
    dist_from_p2, _ = bfs(G1, N1, pos2)
    # G2
    _, pos3 = bfs(G2, N2, 0)
    dist_from_p3, pos4 = bfs(G2, N2, pos3)
    dist_from_p4, _ = bfs(G2, N2, pos4)
    # 直径と距離が等しい2点から距離のうち大きいほう
    dist_g1 = [max(i, j) for i, j in zip(dist_from_p1, dist_from_p2)]
    dist_g2 = [max(i, j) for i, j in zip(dist_from_p3, dist_from_p4)]
    max_dist = max(max(dist_g1), max(dist_g2))
    # ２重for -> O(NN)
    # 累積和的なものを考える -> A[i] := 距離i以下の頂点の距離の合計
    # G2の頂点jの距離でパターン分け(dg1 := g1の直径)
    # 1) D[j] < max(dg1, dg2)
    #   max(dg1, dg2) - D[j]以下の距離の頂点は全てmax(dg1, dg2)
    # 2) max(dg1, dg2) <= D[j]
    # 距離は常にD[i] + D[j] + 1
    cnt = [0] * (max_dist+1)
    for i in range(N2):
        cnt[dist_g2[i]] += 1
    tmp = [i * d for i, d in enumerate(cnt, start=1)]
    cumsum_sumd = [0] + list(accumulate(tmp))
    cumsum_cnt = [0] + list(accumulate(cnt))
    sum_dist = [0] * (N1+1)
    sum_dist = [0] * (max_dist+1)
    for d1 in range(max_dist+1):
        # d1を固定する
        # max(d1+1+d2, max_dist)なので
        # 1) d2 <= max_dist - d1+1
        # 2) max_dist - d1+1 < d2
        # の2パターンになる
        threshold = max(max_dist - (d1+1), 0)
        upper = cumsum_cnt[threshold+1]
        lower = N2 - upper
        # 1) f(i, j) = max_dist
        p1 = upper * max_dist
        # 2) f(i, j) = d1 + d2 + 1
        p2 = lower * d1 + cumsum_sumd[-1] - cumsum_sumd[threshold+1]
        sum_dist[d1] = p1 + p2
    
    # output
    res = 0
    for d1 in dist_g1:
        res += sum_dist[d1]
    print(res)

if __name__ == '__main__':
    main()