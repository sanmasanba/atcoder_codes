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
    N, D = map(int, input().split())
    LR = [tuple(map(int, input().split())) for _ in range(N)]
    LR = deque(sorted(LR, key=lambda x: (x[1], x[0])))
    
    res = 0
    while LR:
        (_, r0) = LR.popleft()
        res += 1
        while LR:
            (l1, r1) = LR[0]
            if l1 <= r0+D-1:
                LR.popleft()
            else:
                break
    print(res)

if __name__ == '__main__':
    main()