# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

def is_out_of_range(x:int, y:int, Xmi:int, Xma:int, Ymi:int, Yma:int) -> bool:
    return not (Xmi <= x < Xma and Ymi <= y < Yma)

# main
def main():
    # intput
    H, W = map(int, input().split())
    S = [list(input().strip()) for _ in range(H)]
    painted = [[INF]*W for _ in range(H)]
    q = deque()
    for h in range(H):
        for w in range(W):
            if S[h][w] == '#': 
                painted[h][w] = 0
                q.append((h, w))

    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    def check(h, w, turn):
        cnt = 0
        for dh, dw in d:
            nh, nw = h+dh, w+dw
            if is_out_of_range(nh, nw, 0, H, 0, W): continue
            if painted[nh][nw] <= turn: cnt += 1
        return cnt == 1

    while q:
        ch, cw = q.popleft()
        turn = painted[ch][cw]
        for dh, dw in d:
            nh, nw = ch+dh, cw+dw
            if is_out_of_range(nh, nw, 0, H, 0, W): 
                continue
            if painted[nh][nw] != INF or not check(nh, nw, turn): 
                continue
            painted[nh][nw] = turn + 1
            q.append((nh, nw))
    
    print(sum(painted[h][w] != INF for h in range(H) for w in range(W)))
            
if __name__ == '__main__':
    main()