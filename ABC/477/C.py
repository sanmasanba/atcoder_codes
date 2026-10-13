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
    S = list(input().strip())
    T = list(input().strip())
    N, M = len(S), len(T)

    ok = [0] * N
    def check(i):
        if N < i + M:
            return 0
        for j in range(M):
            if S[i+j] != T[j]:
                return 0
        return 1
        
    for i in range(N):
        ok[i] = check(i)
    cumsum = [0] + list(accumulate(ok))
    
    for _ in range(Q):
        L, R = map(lambda x: int(x)-1, input().split())
        R -= M - 1
        if R < L:
            print('No')
            continue

        if cumsum[R+1] - cumsum[L] > 0:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()
