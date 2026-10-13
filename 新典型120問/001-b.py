# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, isqrt, pi, gcd, lcm, factorial
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
    Q = int(input())

    h = []
    a = deque()
    for _ in range(Q):
        A = list(map(int, input().split()))

        if A[0] == 1:
            a.append(A[1])
        elif A[0] == 2:
            if 0 < len(h):
                print(heappop(h))
            else:
                print(a[0])
                a.popleft()
        else:
            while a:
                heappush(h, a.popleft())

if __name__ == '__main__':
    main()
