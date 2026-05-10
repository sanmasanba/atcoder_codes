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

#main
def main():
    # intput
    N, H, M = map(int, input().split())
    A, B = zip(*[list(map(int, input().split())) for _ in range(N)])
    
    # dp1 := 体力がhのときの最大魔力m
    # dp2 := 魔力がmのときの最大体力h
    dp1 = [-1] * (H+1)
    dp2 = [-1] * (M+1)
    dp1[-1] = M
    dp2[-1] = H
    for n, (h, m) in enumerate(zip(A, B)):
        hok, mok = False, False
        ndp1 = [-1]*(H+1)
        ndp2 = [-1]*(M+1)
        for i in range(H, -1, -1):
            # 体力iのとき、魔力をmだけ使って敵を倒す
            if m <= dp1[i]:
                ndp1[i] = max(dp1[i] - m, ndp1[i])
                ndp2[ndp1[i]] = max(i, ndp2[ndp1[i]])
                hok = True
        for j in range(M, -1, -1):
            # 魔力jのとき、体力をhだけ使って敵を倒す
            if h <= dp2[j]:
                mok = True
                ndp2[j] = max(dp2[j] - h, ndp2[j])
                ndp1[ndp2[j]] = max(j, ndp1[ndp2[j]])
        dp1 = ndp1
        dp2 = ndp2
        if not hok and not mok:
            print(n)
            return
    print(N)

if __name__ == '__main__':
    main()