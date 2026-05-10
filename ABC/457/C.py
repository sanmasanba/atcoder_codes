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
    LA = [list(map(lambda x: int(x), input().split())) for _ in range(N)]
    C = list(map(int, input().split()))
    
    b = 0
    for i, ci in enumerate(C):
        li = LA[i][0]
        if K <= b + ci*li:
            ok = 0
            ng = ci+1
            while ng-ok>1:
                mi = (ok+ng)//2
                if K <= b+mi*li:
                    ng = mi
                else:
                    ok = mi
            r = K-(b+ok*li)
            print(LA[i][r])
            return
        else:
            b += ci*li

if __name__ == '__main__':
    main()