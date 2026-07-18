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
    H, W = map(int, input().split())
    S = [list(input().strip()) for _ in range(H)]
    T = [[-1 for _ in range(W)] for _ in range(H)]

    dxs = [1, 1, 0, -1, -1, -1, 0, 1]
    dys = [0, 1, 1, 1, 0, -1, -1, -1]
    # 1) 1ターンだけ進める
    queue = deque()
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.': continue
            for i in range(8):
                nh, nw = h+dxs[i], w+dys[i]
                if not (0 <= nh < H and 0 <= nw < W):
                    continue
                if S[nh][nw] == '.':
                    T[nh][nw] = 0
    for h in range(H):
        for w in range(W):
            if T[h][w] == 0: queue.append((h, w))

    # BFS
    def bfs():
        while queue:
            (h, w) = queue.popleft()
            for i in range(8):
                nh, nw = h+dxs[i], w+dys[i]
                if not (0 <= nh < H and 0 <= nw < W):
                    continue
                if 0 <= T[nh][nw]:
                    continue
                T[nh][nw] = T[h][w] + 1
                queue.append((nh, nw))
    
    bfs()
    print(*[''.join('#' if tt%2 and tt!=-1 else '.' for tt in t) for t in T], sep='\n')

if __name__ == '__main__':
    main()