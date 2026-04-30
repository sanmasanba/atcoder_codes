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

# 文字列の指定がないときはmove2dを消す
d2moveR = {0:'U', 1: 'R', 2: 'D'}
d2moveL = {0:'U', 1: 'L', 2: 'D'}
dR = [[-1, 0], [0, 1], [1, 0]]
dL = [[-1, 0], [0, -1], [1, 0]]

def solve():
    N, A, B = map(int, input().split())
    if N%2 == 1:
        print('No')
        return
    if N%2 == 0 and (A+B)%2 == 0:
        print('No')
        return
    
    res = []
    seen = [[0]*N for _ in range(N)]
    seen[A-1][B-1], seen[0][0] = 1, 1
    hr, hc = 0, 0
    flg = 0
    while (hr, hc) != (N-1, N-1):
        while 1:
            if (flg == 0 and hc == N-1):
                break
            if (flg == 1 and hc == 0):
                break
            for dir, (dr, dc) in enumerate(dR if flg%2==0 else dL):
                nh , nc = hr+dr, hc+dc
                if not(0 <= nh < N and 0 <= nc < N) or seen[nh][nc]:
                    continue
                res.append(d2moveR[dir] if flg%2==0 else d2moveL[dir])
                seen[nh][nc] = 1
                hr, hc = nh, nc
                break
            if (hr, N-1 if flg else 0) == (A-1, B-1):
                break
            if (hr, hc) == (N-1, N-1):
                break
        flg ^= 1

    print('Yes')
    print(''.join(res))

# main
def main():
    # intput
    T = int(input())
    for _ in range(T): solve()

if __name__ == '__main__':
    main()