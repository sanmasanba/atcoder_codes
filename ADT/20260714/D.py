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
    N = int(input())
    A = [list(map(int, list(input().strip()))) for _ in range(N)]

    res = 0
    dxs = [1, 1, 0, -1, -1, -1, 0, 1]
    dys = [0, 1, 1, 1, 0, -1, -1, -1]
    for h in range(N):
        for w in range(N):
            for dh, dw in zip(dxs, dys):
                tmp = 0
                for i in range(N):
                    tmp = tmp*10 + A[(h+i*dh)%N][(w+i*dw)%N]
                res = max(res, int(tmp))
    print(res)

if __name__ == '__main__':
    main()