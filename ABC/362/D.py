#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    N, M = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    G = {}
    for _ in range(M):
        s, g, weight = map(int, input().split(' '))
        if s-1 not in G:
            G[s-1] = {}
        G[s-1][g-1] = weight
        if g-1 not in G:
            G[g-1] = {}
        G[g-1][s-1] = weight
    
    # dist:vからの距離, queue:探索キュー
    dist = [INF for _ in range(N)]
    queue = deque()
    dist[0] = A[0]
    queue.append(0)

    while queue:
        # 探索開始ノード
        v = queue.popleft()
        # vから延びるノードを探索
        for next_v, next_weight in G[v].items():
            # 更新可能なら更新して、次のノードを探索
            if dist[next_v] > dist[v] + A[next_v] + next_weight:
                dist[next_v] = dist[v]+A[next_v]+next_weight
                queue.append(next_v)
                
    # 出力
    for v in range(1, N):
        print(dist[v], end=' ')

if __name__ == '__main__':
    main()