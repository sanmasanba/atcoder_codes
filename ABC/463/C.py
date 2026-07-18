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
    tmp = defaultdict(int)
    for _ in range(N):
        H, L = map(int, input().split())
        tmp[L] = max(tmp[L], H)
    tmp = sorted([[l, h] for l, h in tmp.items()], reverse=True)
    ma_hs = []
    ma = 0
    for l, h in tmp:
        ma = max(ma, h)
        ma_hs.append(([l, ma]))
    ma_hs.reverse()
    Q = int(input())
    res = []
    for i, t in enumerate(map(int, input().split())):
        item = bisect_right(ma_hs, t, key=lambda x: x[0])
        res.append(ma_hs[item][1])
    print(*res, sep='\n')

if __name__ == '__main__':
    main()