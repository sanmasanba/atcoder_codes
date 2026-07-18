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
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x: (x[1], x[0]))

    def solver(x):
        k = 0
        ma = -x
        for i in range(N):
            l, r = LR[i]
            if (l-ma) >= x:
                ma = r
                k += 1
            if k == K:
                return True
        return False
    
    ok = 0
    ng = 1 << 64
    while ng-ok > 1:
        mi = (ng+ok)//2
        
        if solver(mi):
            ok = mi
        else:
            ng = mi
    print(ok if ok > 0 else -1)

if __name__ == '__main__':
    main()