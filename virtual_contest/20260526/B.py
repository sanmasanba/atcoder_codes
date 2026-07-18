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

    res = [[-1]*W for _ in range(H)]
    buf = deque()
    for h in range(H):
        for w in range(W):
            if S[h][w] == '#': 
                res[h][w] = 0
                buf.append((h, w))            

    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    def is_out_of_range(x:int, y:int, Xmi:int, Xma:int, Ymi:int, Yma:int) -> bool:
        return not (Xmi <= x < Xma and Ymi <= y < Yma)
    
    while buf:
        h, w = buf.popleft()
        turn = res[h][w]
        for (_h, _w) in d:
            hh, ww = h+_h, w+_w
            if is_out_of_range(hh, ww, 0, H, 0, W) or -1 < res[hh][ww]:
                continue
            cnt = 0
            for (dh, dw) in d:
                nh, nw = hh+dh, ww+dw
                if is_out_of_range(nh, nw, 0, H, 0, W):
                    continue
                cnt += 0 <= res[nh][nw] <= turn
            if cnt == 1:
                res[hh][ww] = turn + 1
                buf.append((hh, ww))
    
    ans = 0
    for h in range(H):
        for w in range(W):
            ans += 0 <= res[h][w]
    print(ans)

if __name__ == '__main__':
    main()