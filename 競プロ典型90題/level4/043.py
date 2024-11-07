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
    
def main():
    H, W = map(int, input().split(' '))
    rs, cs = map(lambda x: int(x)-1, input().split(' '))
    rt, ct = map(lambda x: int(x)-1, input().split(' '))
    S = []
    # マップを一次元で表現
    dist = [INF] * (H * W * 4)
    for _ in range(H):
        S.append(list(input()))

    que = deque([(rs, cs, i) for i in range(4)])
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # init dist
    for i in range(4):
        dist[rs*W*4 + cs*4 + i] = 0
    for r in range(H):
        for c in range(W):
            if S[r][c] == '#':
                for i in range(4):
                    dist[r*W*4+c*4+i] = -1

    while que:
        r, c, orient = que.popleft()
        for i, (dr, dc) in enumerate(d):
            nr = r + dr
            nc = c + dc            
            if not (0 <= nr < H and 0 <= nc < W):
                continue
            if dist[nr*W*4+nc*4+i] == -1:
                continue

            # 更新があれば、再度探索
            if orient == i:
                if dist[nr*W*4+nc*4+i] > dist[r*W*4+c*4+orient]:
                    dist[nr*W*4+nc*4+i] = dist[r*W*4+c*4+orient]
                    que.appendleft((nr, nc, i))
            else:
                if dist[nr*W*4+nc*4+i] > dist[r*W*4+c*4+orient] + 1:
                    dist[nr*W*4+nc*4+i] = dist[r*W*4+c*4+orient] + 1
                    que.append((nr, nc, i))
    
    res = INF
    for i in range(4):  
        if dist[rt*W*4+ct*4+i] == -1:
            continue
        res = min(res, dist[rt*W*4+ct*4+i])
    print(res)

if __name__ == '__main__':
    main()
        
