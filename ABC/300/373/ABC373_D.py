#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, M = map(int, input().split())
    G = defaultdict(dict)
    for _ in range(M):
        s, g, weight = map(int, input().split())
        s -= 1
        g -= 1
        G[s][g] = weight
        G[g][s] = -weight

    visited = [False] * N
    res = [0] * N

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            queue = deque([i])
            while queue:
                u = queue.popleft()
                for v, weight in G[u].items():
                    if not visited[v]:
                        res[v] = res[u] + weight
                        visited[v] = True
                        queue.append(v)
    
    print(*res)

if __name__ == '__main__':
    main()