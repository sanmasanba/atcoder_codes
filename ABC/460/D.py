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
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

INF = 1000000010
# main
def main():
    # intput
    H, W = map(int, input().split())
    S = [list(input().strip()) for _ in range(H)]
    dxs = [1, 1, 0, -1, -1, -1, 0, 1]
    dys = [0, 1, 1, 1, 0, -1, -1, -1]
    
    in_range = lambda x, y: (0 <= x < H) and (0 <= y < W)

    B = [['.']*W for _ in range(H)] 
    for h in range(H):
        for w in range(W):
            if S[h][w] == '#':
                for (dh, dw) in zip(dxs ,dys):
                    nh, nw = h+dh, w+dw
                    if in_range(nh, nw) and S[nh][nw]=='.':
                        B[nh][nw] = '#'
    S = B

    D = [[INF]*W for _ in range(H)]
    Q = deque()
    for h in range(H):
        for w in range(W):
            if S[h][w]=='#': 
                D[h][w] = 0
                Q.append((h, w))
    while Q:
        (h, w) = Q.popleft()
        for (dh, dw) in zip(dxs, dys):
            nh, nw = h+dh ,w+dw
            if in_range(nh, nw) and D[nh][nw] == INF:
                D[nh][nw] = D[h][w] + 1
                Q.append((nh, nw))

    for h in range(H):
        for w in range(W):
            S[h][w] = '.' if D[h][w] % 2 == 0 else '#'
        print(''.join(S[h]))

if __name__ == '__main__':
    main()