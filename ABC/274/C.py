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
    N = int(input())
    A = list(map(int, input().split(' ')))
    
    # 二分木にする
    G = {}
    for i, a in enumerate(A, start=1):
        G[a] = [2*i, 2*i+1]
    
    #BFS
    def bfs(s):
        # dist:vからの距離, queue:探索キュー
        dist = [-1 for _ in range(2*(N+1))]
        queue = deque()
        dist[s] = 0
        queue.append(s)
        while queue:
            v = queue.popleft()
            if v not in G:
                continue
            for next_v in G[v]:
                if dist[next_v] != -1:
                    continue
                dist[next_v] = dist[v] + 1
                queue.append(next_v)
        return dist

    res = bfs(1)
    for r in res[1:]:
        print(r)

if __name__ == '__main__':
    main()