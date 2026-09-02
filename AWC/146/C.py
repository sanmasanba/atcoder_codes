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
    N, M, K = map(int, input().split())
    L = list(map(int, input().split()))

    tmp = [0]*(N+1)
    for _ in range(M):
        X, Y, Z = map(int, input().split())
        tmp[X-1] += Z
        tmp[Y] -= Z
    cumsum = [0] + list(accumulate(tmp))

    print(len([1 for l, c in zip(L, cumsum[1:]) if K <= l+c]))

if __name__ == '__main__':
    main()
