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
    C = deque([deque(input().strip()) for _ in range(H)])

    while C:
        f = False
        if C and all(c == '.' for c in C[0]):
            C.popleft()
            f = True
        if C and all(c == '.' for c in C[-1]):
            C.pop()
            f = True
        if C and all(c[-1] == '.' for c in C):
            for c in C: c.pop()
            f = True
        if C and all(c[0] == '.' for c in C):
            for c in C: c.popleft()
            f = True
        if not f:
            break

    for c in C:
        print(''.join(c))

if __name__ == '__main__':
    main()