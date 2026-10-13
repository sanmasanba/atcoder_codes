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
    N, S, L = map(int, input().split())
    S -= 1
    A = list(map(int, input().split())) + [INF]
    cumsum = [0] + list(accumulate(A))
    
    res = 1
    # 右移動からのめいいっぱい左
    for ok in range(S, N):
        ng = -1
        if L < cumsum[ok] - cumsum[S]:
            continue
        l = L - (cumsum[ok] - cumsum[S])
        right = ok
        while ok - ng > 1:
            mi = (ok + ng) // 2
            if cumsum[right] - cumsum[mi] <= l:
                ok = mi
            else:
                ng = mi
        res = max(res, right - min(ok, S) + 1)
    # 左移動からのめいいっぱい右
    for ok in range(S, -1, -1):
        ng = N+1
        if L < cumsum[S] - cumsum[ok]:
            continue
        l = L - (cumsum[S] - cumsum[ok])
        left = ok
        while ng - ok > 1:
            mi = (ok + ng) // 2
            if cumsum[mi] - cumsum[left] <= l:
                ok = mi
            else:
                ng = mi
        res = max(res, max(S, ok) - left + 1)
    print(res)

if __name__ == '__main__':
    main()
