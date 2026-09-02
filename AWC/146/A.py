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
    N, M, Q = map(int, input().split())
    S, U, F = zip(*[list(map(int, input().split())) for _ in range(N)])
    S, U, F = list(S), list(U), list(F)

    for _ in range(Q):
        d, c = input().strip().split()
        d = int(d) - 1
        if c == '+':
            if S[d] < M:
                U[d], F[d] = 7 - F[d], U[d]
                S[d] += 1
        elif c == '-':
            if 1 < S[d]:
                U[d], F[d] = F[d], 7 - U[d]
                S[d] -= 1
    
    for s, u in zip(S, U):
        print(s, u)    

if __name__ == '__main__':
    main()
