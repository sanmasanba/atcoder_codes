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
    S = list(input().strip())
    T = []
    for s in S:
        T.append(s)
        T.append(' ')
    T.pop()
    N = len(T)
    
    def check(m):
        tmp = 0
        res = 0
        for k in range(N):
            if m-k < 0 or N <= m+k:
                return res
            tmp += T[m-k] != T[m+k]
            if 1 < tmp:
                return res
            if not (T[m-k] == ' ' and T[m+k] == ' '):
                res += 1
        return res

    res = 0
    for m in range(N):
        res += check(m)
    print(res)

if __name__ == '__main__':
    main()