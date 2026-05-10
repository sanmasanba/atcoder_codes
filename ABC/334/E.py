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
MOD = 998244353

#main
def main():
    # intput
    H, W = map(int, input().split())
    S = [['x']*(W+2)]
    for _ in range(H):
        S.append(['x']+list(input())+['x'])
    S.append(['x']*(W+2))
    
    CC = 0
    dist = [[-1]*(W+2) for _ in range(H+2)]
    for w in range(W+2): dist[0][w] = INF
    for w in range(W+2): dist[-1][w] = INF
    for h in range(H+2): 
        dist[h][0] = INF
        dist[h][-1] = INF
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def is_out_of_range(x:int, y:int, Xmi:int, Xma:int, Ymi:int, Yma:int) -> bool:
        return not (Xmi <= x < Xma and Ymi <= y < Yma)

    def bfs(sh, sw, CC):
        queue = deque()
        dist[sh][sw] = CC
        queue.append((sh, sw))
        while queue:
            h, w = queue.popleft()
            for dh, dw in d:
                nh = h+dh
                nw = w+dw
                if is_out_of_range(nh, nw, 0, len(S), 0, len(S[0])):
                    continue
                if dist[nh][nw] != -1 or S[nh][nw] == '.':
                    continue
                dist[nh][nw] = dist[h][w]
                queue.append((nh, nw))
    
    for h in range(H+2):
        for w in range(W+2):
            if S[h][w] == '.' or S[h][w] == 'x':
                dist[h][w] = INF
            elif dist[h][w] == -1:
                bfs(h, w, CC)
                CC += 1

    def check(h, w):
        cnt = set()
        for dh, dw in d:
            nh = h+dh
            nw = w+dw
            if S[nh][nw] == '#':
                cnt.add(dist[nh][nw])
        return len(cnt)

    res = []
    for h in range(1, H+1):
        for w in range(1, W+1):
            if S[h][w] == '.':
                res.append(CC+1-check(h, w))

    # output
    over = sum(k*v for k, v in Counter(res).items())
    base = len(res)
    print(over*pow(base, MOD-2, MOD)%MOD)

if __name__ == '__main__':
    main()