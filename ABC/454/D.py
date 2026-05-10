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

def stack(items):
    res = []
    for item in items:
        res.append(item)
        if 3 < len(res) and res[-4:] == ['(', 'x', 'x', ')']:
            for _ in range(4): res.pop()
            res.extend(['x', 'x'])
    return res

def solve():
    A = deque(input().strip())
    B = deque(input().strip())

    if stack(A) == stack(B):
        print('Yes')
    else:
        print('No')

# main
def main():
    # intput
    T = int(input())
    for _ in range(T): solve()

if __name__ == '__main__':
    main()