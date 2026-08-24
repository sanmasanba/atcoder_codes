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
# m本の辺からn-1本を選ぶ　→　mC(n-1) は計算できない
# 最短経路を選ぶ方法を考える
# 重み付き最短経路はダイクストラを使う
# →　辺をどう復元するか？
# 自分がどこから来た辺かを覚えておけば復元できる
# 更新時に親ノードさえ記録しておけば、O((n+m)logm)

# main
def main():
    # intput
    N, M = map(int, input().split())
    G = defaultdict(list)
    for i in range(1, M+1):
        s, g, weight = map(int, input().split())
        G[s].append((g, weight, i))
        G[g].append((s, weight, i))

    def dijkstra(G, N, s):
        distances = [INF] * N
        parent_edge = [-1] * N
        distances[s] = 0
    
        target_nodes = []
        heappush(target_nodes, (0, s))
    
        while target_nodes:
            current_dist, current_node = heappop(target_nodes)
    
            if current_dist > distances[current_node]:
                continue
    
            for next_node, weight, edge in G[current_node]:
                dist = current_dist + weight
                if dist < distances[next_node]:
                    distances[next_node] = dist
                    parent_edge[next_node] = edge
                    heappush(target_nodes, (dist, next_node))
    
        return parent_edge

    edegs = dijkstra(G, N+1, 1)
    res = [edegs[i] for i in range(2, N+1)]
    print(*res)

if __name__ == '__main__':
    main()
