#library
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

# 341_C
# main
def main():
    # intput
    H, W, N = map(int, input().split())
    T = input().strip()
    S = []
    for _ in range(H):
        tmp = list(input().strip())
        S.extend(tmp)

    move2d = {'U':0, 'D':1, 'L':2, 'R':3}
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    def bfs(h, w):
        p = h*W + w
        if S[p] == '#': return False
        for t in T:
            h, w = h+d[move2d[t]][0], w+d[move2d[t]][1]
            p = h*W + w
            if S[p] == '#': return False
        return True

    res = 0
    for h in range(1, H-1):
        for w in range(1, W-1):
            res += 1 if bfs(h, w) else 0
    print(res)


if __name__ == '__main__':
    main()