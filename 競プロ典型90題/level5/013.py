#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

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

#main
def main():
    # intput
    N, M = map(int, input().split(' '))
    G = defaultdict(list)
    for _ in range(M):
        s, g, weight = map(int, input().split(' '))
        G[s-1].append((g-1, weight))
        G[g-1].append((s-1, weight))
    
    from_0_dist = dijkstra(G, N, 0)
    from_N_dist = dijkstra(G, N, N-1)

    for i in range(N):
        print(from_0_dist[i] + from_N_dist[i])

if __name__ == '__main__':
    main()