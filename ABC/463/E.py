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

# main
def main():
    # intput
    N, M, Y = map(int, input().split())
    G = defaultdict(list)
    for _ in range(M):
        s, g, weight = map(int, input().split())
        G[s-1].append((g-1, weight))
        G[g-1].append((s-1, weight))
    X = list(map(int, input().split()))
    
    # 解法
    # 1) どのワープもY分追加でかかる -> どの都市からでても同じ経路を通過する
    # 2) ワープの両端を新たな都市として、そこに向かう経路をXi, Xjとする
    #    i - Xi+Xj+Y -> j を i -Xi-> new1 -Y-> new2 -Xj-> j に分解する
    # dijkstraを解けば答え
    
    # new1 -> new2 を追加
    G[N].append((N+1, Y))
    # i -> new1, new2 -> i を追加
    for i in range(N):
        G[i].append((N, X[i]))
        G[N+1].append((i, X[i]))

    def dijkstra(G, N, s):
        distances = [INF] * N
        distances[s] = 0
    
        target_nodes = []
        heappush(target_nodes, (0, s))
    
        while target_nodes:
            current_dist, current_node = heappop(target_nodes)
    
            if current_dist > distances[current_node]:
                continue
    
            for next_node, weight in G[current_node]:
                dist = current_dist + weight
                if dist < distances[next_node]:
                    distances[next_node] = dist
                    heappush(target_nodes, (dist, next_node))
    
        return distances
    
    print(*dijkstra(G, N+2, 0)[1:-2])

if __name__ == '__main__':
    main()