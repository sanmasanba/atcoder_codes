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

#main
def main():
    # intput
    N, M, K = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    nodes = [-1]*N    
    queue = []
    for i in range(K):
        p ,h = map(int, input().split())
        nodes[p-1] = h
        heappush(queue, (-h, p-1))

    #BFS
    def bfs():
        while queue:
            h, v = heappop(queue)
            h *= -1
            # より体力の高い警備員が到達可能なら無視する
            if h < nodes[v]:
                continue
            for next_v in G[v]:
                # より体力を残して到達可能なら移動
                if nodes[next_v] < h-1:
                    nodes[next_v] = h-1
                    if h-1 > 0:
                        heappush(queue, (-h+1, next_v))
    bfs()

    res = [i+1 for i, c in enumerate(nodes) if 0 <= c]
    print(len(res))
    print(*res)

if __name__ == '__main__':
    main()