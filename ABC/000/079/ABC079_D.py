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
    H, W = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(10)]
    A = [list(map(int, input().split())) for _ in range(H)]

    def dijkstra(N, s):
        distances = [INF] * N
        distances[s] = 0
    
        target_nodes = []
        heappush(target_nodes, (0, s))
    
        while target_nodes:
            current_dist, current_node = heappop(target_nodes)
    
            if current_dist > distances[current_node]:
                continue
    
            for next_node in range(N):
                if current_node == next_node:
                    continue
                weight = C[current_node][next_node]
                dist = current_dist + weight
                if dist < distances[next_node]:
                    distances[next_node] = dist
                    heappush(target_nodes, (dist, next_node))
    
        return distances

    dist = [dijkstra(10, i) for i in range(10)]

    res = 0
    for i in range(H):
        for j in range(W):
            if A[i][j] < 0:
                continue
            res += dist[A[i][j]][1]
    print(res)

if __name__ == '__main__':
    main()