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
    H, W = map(int, input().split())
    S = [['#']*(W+2)]
    for _ in range(H):
        input_ = ['#'] + list(input()) + ['#']
        S.append(input_)
    S.append(['#']*(W+2))

    # SとGを探す
    for h in range(H+2):
        for w in range(W+2):
            if S[h][w] == 'S':
                start = (h, w)
            if S[h][w] == 'G':
                goal = (h, w)
    
    d = {0:[[-1, 0], [1, 0]], 1:[[0, -1], [0, 1]]}
    seen = set()
    res = INF
    #BFS
    def bfs(s, g, direction):
        dist = [[-1]*(W+2) for _ in range(H+2)]
        queue = deque()
        dist[s[0]][s[1]] = 0
        queue.append((s, direction))
        while queue:
            v, nd = queue.popleft()
            h, w = v
            for dh, dw in d[nd]:
                nh, nw = h+dh, w+dw
                if g == (nh, nw):
                    return dist[h][w]+1
                if S[nh][nw] == '#':
                    continue
                if dist[nh][nw] != -1:
                    continue
                dist[nh][nw] = dist[h][w] + 1
                queue.append(((nh, nw), 0 if nd else 1))
        return INF

    for direction in range(2):
        res = min(res, bfs(start, goal, direction))
    print(-1 if res == INF else res)

if __name__ == '__main__':
    main()