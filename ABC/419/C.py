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
    N = int(input())
    R, C = [0]*N, [0]*N
    for i in range(N):
        a, b = map(int, input().split())
        R[i] = a
        C[i] = b
    rr = (max(R)+min(R))//2
    cc = (max(C)+min(C))//2
    dxs = [1, 1, 0, -1, -1, -1, 0, 1, 0]
    dys = [0, 1, 1, 1, 0, -1, -1, -1, 0]
    res = INF
    for xx, yy in zip(dxs, dys):
        r0, c0 = max(min(rr+xx, 1e9), -1e9), max(min(cc+yy, 1e9), -1e9)
        tmp = 0
        for ri, ci in zip(R, C):
            tmp = max(abs(r0-ri), abs(c0-ci), tmp)
        res = min(tmp, res)
    print(res)

if __name__ == '__main__':
    main()