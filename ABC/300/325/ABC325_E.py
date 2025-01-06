#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop, heapify
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    # intput
    N, A, B, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(N)]

    def dijkstra(N, s, start, distances, weight, bias=0):
        target_nodes = []
        heappush(target_nodes, (start, s))
    
        while target_nodes:
            current_dist, current_node = heappop(target_nodes)
    
            if current_dist > distances[current_node]:
                continue
    
            for next_node in range(N):
                dist = current_dist+D[current_node][next_node]*weight+bias
                if dist < distances[next_node]:
                    distances[next_node] = dist
                    heappush(target_nodes, (dist, next_node))
    
        return distances

    # 乗用車で最短を求めておく
    distances = [INF] * N
    distances[0] = 0
    dp = dijkstra(N, 0, 0, distances, A)
    
    res = INF
    target_nodes = [(dist, i) for i, dist in enumerate(dp)]
    heapify(target_nodes)
    while target_nodes:
        current_dist, current_node = heappop(target_nodes)

        if current_dist > dp[current_node]:
            continue

        for next_node in range(N):
            dist = current_dist+D[current_node][next_node]*B+C
            if dist < dp[next_node]:
                dp[next_node] = dist
                heappush(target_nodes, (dist, next_node))
    print(dp[-1])

if __name__ == '__main__':
    main()