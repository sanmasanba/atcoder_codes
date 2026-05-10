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

#main
def main():
    # intput
    N, M = map(int, input().split())
    G = defaultdict(lambda: defaultdict(lambda: (1 << 32) - 1))
    for _ in range(M):
        s, g, weight = map(lambda x: int(x)-1, input().split())
        G[s][g] = G[s][g] if G[s][g].bit_count() < (weight+1).bit_count() else weight+1
        G[g][s] = G[g][s] if G[g][s].bit_count() < (weight+1).bit_count() else weight+1

    def dijkstra(N, s=0):
        distances = [INF] * N
        distances[s] = 0
    
        target_nodes = []
        heappush(target_nodes, (0, s))
    
        while target_nodes:
            current_dist, current_node = heappop(target_nodes)
            for next_node, weight in G[current_node].items():
                dist = current_dist | weight
                if dist < distances[next_node]:
                    distances[next_node] = dist
                    heappush(target_nodes, (dist, next_node))
    
        return distances
    
    res = dijkstra(N)
    print(res[-1])

if __name__ == '__main__':
    main()