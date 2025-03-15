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

#main
def main():
    # intput
    N, M, X = map(int, input().split())
    G = defaultdict(set)
    for _ in range(M):
        s, g = map(int, input().split())
        # s -> g
        G[s].add((g, 1))
        # g+N -> s+N
        G[g+N].add((s+N, 1))
        # s -> s+N
        G[s].add((s+N, X))
        # s+N -> s
        G[s+N].add((s, X))
        # g -> g+N
        G[g].add((g+N, X))
        # g+N -> g
        G[g+N].add((g, X))
    # s -> 1
    G[0].add((1, 0))
    # s -> N+1
    G[0].add((1+N, X))
    # N -> g
    G[N].add((2*N+1, 0))
    # 2*N -> g
    G[2*N].add((2*N+1, 0))

    def dijkstra(N, s):
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
    
    dist = dijkstra(2*N+2, 0)
    print(dist[-1])

if __name__ == '__main__':
    main()