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
    H, W = map(int, input().split(' '))
    A = [list(input()) for _ in range(H)]

    N = int(input())
    RCE = {}
    for _ in range(N):
        r, c, e = map(int, input().split(' '))
        RCE[(r-1, c-1)] = e

    s = None
    for h in range(H):
        for w in range(W):
            if A[h][w] == 'S':
                s = (h, w)
                break
        if s is not None:
            break

    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    mp = [[0]*W for _ in range(H)]
    que = deque([s])
    seen = set()
    while que:
        v = que.popleft()
        if v in seen or v not in RCE:
            continue
        seen.add(v)
        
        e = RCE[v]
        queue = deque([v])
        visited = set([v])
        mp[v[0]][v[1]] = 0
        while queue:
            h, w = queue.popleft()
            for dh, dw in d:
                if e <= mp[h][w]:
                    continue
                nh, nw = h+dh, w+dw
                if not (0 <= nh < H and 0 <= nw < W):
                    continue        
                if A[nh][nw] == 'T':
                    print('Yes')
                    return
                
                if A[nh][nw] == '.' and (nh, nw) not in visited:
                    visited.add((nh, nw))
                    mp[nh][nw] = mp[h][w] + 1
                    if (nh, nw) in RCE and (nh, nw) not in seen:
                        que.append((nh, nw))
                    queue.append((nh, nw))

    print('No')

if __name__ == '__main__':
    main()