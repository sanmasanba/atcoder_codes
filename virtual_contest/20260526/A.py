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
    
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    def comp(h, w, s):
        tmp = {s:i for i, s in enumerate(['^', 'v', '<', '>'])}
        dh, dw = d[tmp[s]]
        while 1:
            h = h + dh
            w = w + dw
            if not(0 <= h < H and 0 <= w < W) or S[h][w] in ('#', '^', 'v', '<', '>'):
                return
            if S[h][w] == '.': 
                S[h][w] = '!'

    for h in range(H):
        for w in range(W):
            if S[h][w] in ('^', 'v', '<', '>'):
                comp(h, w, S[h][w])
            if S[h][w] == 'S':
                sh, sw = h, w
            if S[h][w] == 'G':
                gh, gw = h, w            
    
    # BFS
    def bfs(sh, sw, gh, gw):
        # dist:vからの距離, queue:探索キュー
        dist = [[-1]*W for _ in range(H)]
        queue = deque()
        dist[sh][sw] = 0
        queue.append((sh, sw))
        while queue:
            h, w = queue.popleft()
            for (dh, dw) in d:
                nh, nw = h+dh, w+dw
                if not(0 <= nh < H and 0 <= nw < W) or dist[nh][nw] != -1:
                    continue
                if S[nh][nw] not in ('.', 'S', 'G'):
                    continue
                dist[nh][nw] = dist[h][w] + 1
                queue.append((nh, nw))
        return dist[gh][gw]
        
    print(bfs(sh, sw, gh, gw))

if __name__ == '__main__':
    main()