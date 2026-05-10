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
    N, Q = map(int, input().split())
    roots = [0 for i in range(N+1)]
    
    for _ in range(Q):
        C, P = map(int, input().split())
        roots[C] = P
    
    is_top = [True for _ in range(N+1)]
    for i in range(N+1):
        is_top[roots[i]] = False

    res = [0] * N
    for top, f in enumerate(is_top):
        if not f: continue
        tmp = 0
        while 1:
            tmp += 1
            if roots[top] == 0:
                res[top-1] = tmp
                break
            top = roots[top]
    print(*res)

if __name__ == '__main__':
    main()