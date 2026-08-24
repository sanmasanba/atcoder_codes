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
    Q, V = map(int, input().split())
    h = []

    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            _, t, w = query
            heappush(h, -(w - t))
        elif query[0] == 2:
            _, t = query
            if h:
                w = heappop(h)
                print(min(V, -w + t))
            else:
                print(-1)

if __name__ == '__main__':
    main()
