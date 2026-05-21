# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple, OrderedDict
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
    A = sorted(list(map(int, input().split())))
    ce = max(A)

    cnt = Counter(A)
    
    res = 0
    for r in range(1, ce+1):
        q = 1
        while r*q <= ce: 
            res += cnt.get(r, 0) * cnt.get(q, 0) * cnt.get(r*q, 0)
            q += 1
    print(res)

if __name__ == '__main__':
    main()