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

# DFS
seen = set()
def dfs(h, w, dist):
    global res
    if dist == K:
        res += 1
        return
    seen.add((h, w))
    # 探索
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for dh, dw in d:
        nh = h + dh
        nw = w + dw
        if (nh, nw) in seen or is_out_of_range(nh, nw, 0, H, 0, W):
            continue
        if S[nh][nw] == '#':
            continue
        dfs(nh, nw, dist + 1)
    seen.remove((h, w))

#main
def main():
    # intput
    global H, W, K
    H, W, K = map(int, input().split(' '))
    global S
    S = [list(input()) for _ in range(H)]

    global res
    res = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                dfs(i, j, 0)
    print(res)

if __name__ == '__main__':
    main()