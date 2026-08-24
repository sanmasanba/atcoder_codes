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
    N, X, Y = map(int, input().split())
    r = [0]*11
    r[N] = 1
    b = [0]*11
    for i in range(N, 1, -1):
        if 0 < r[i]:
            r[i-1] += r[i]
            b[i] += X * r[i]
        if 0 < b[i]:
            r[i-1] += b[i]
            b[i-1] += Y * b[i]
    print(b[1])

if __name__ == '__main__':
    main()