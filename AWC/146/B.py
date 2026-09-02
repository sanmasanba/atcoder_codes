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
    S = [list(map(int, input().split())) for _ in range(H)]

    sumH = list(sum(i) for i in S)
    sumW = list(sum(i) for i in zip(*S))

    res = -INF
    for h in range(H):
        for w in range(W):
            res = max(res, sumH[h]+sumW[w]-S[h][w])
    print(res)

if __name__ == '__main__':
    main()
