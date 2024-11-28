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

def is_out_of_range(x:int, y:int, Xmi:int, Xma:int, Ymi:int, Yma:int) -> bool:
    if Xmi <= x < Xma and Ymi <= y < Yma:
        return False
    else:
        return True

def search_S(H, W):
    for h in range(H):
        for w in range(W):
            if C[h][w] == 'S':
                return [h, w]

#main
def main():
    # intput
    global C
    H, W = map(int, input().split(' '))
    C = [list(input()) for _ in range(H)]

    sh, sw = search_S(H, W)
    
    dhs = [0, 1, 0, -1]
    dws = [1, 0, -1, 0]
    dist = [-1 for _ in range(H*W)]
    parent = [-1 for _ in range(H*W)]
    
    dist[sh*W+sw] = 0
    parent[sh*W+sw] = INF
    que = deque()
    for dh, dw in zip(dhs, dws):
        nh, nw = sh+dh, sw+dw
        if is_out_of_range(nh, nw, 0, H, 0, W):
            continue
        if C[nh][nw] == '#':
            continue
        if parent[nh*W+nw] == INF:
            continue
        dist[nh*W+nw] = 1
        parent[nh*W+nw] = dh*W+dw
        que.append((sh+dh, sw+dw))

    res = False
    while que and not res:
        h, w = que.popleft()
        p = parent[h*W+w]
        for dh, dw in zip(dhs, dws):
            nh, nw = h+dh, w+dw
            # 無視する
            if is_out_of_range(nh, nw, 0, H, 0, W):
                continue
            if C[nh][nw] == '#':
                continue
            if parent[nh*W+nw] == INF:
                continue

            # 到達していないならキューに追加
            if dist[nh*W+nw] == -1:
                dist[nh*W+nw] = dist[h*W+w]+1
                que.append([nh, nw])
                parent[nh*W+nw] = p
                continue

            # 到達済みなら条件判定
            if parent[nh*W+nw] != p and 4 <= dist[nh*W+nw]+dist[h*W+w]+1:
                res = True

    print('Yes' if res else 'No')

if __name__ == '__main__':
    main()