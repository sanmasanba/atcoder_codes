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
    N, M = map(int, input().split())
    S = [list(input().strip()) for _ in range(N)]
    T = [list(input().strip()) for _ in range(M)]

    def solve(a, b):
        for i in range(M):
            for j in range(M):
                if S[a+i][b+j] != T[i][j]:
                    return False
        return True

    for a in range(N-M+1):
        for b in range(N-M+1):
            if solve(a, b):
                print(a+1, b+1)
                return

if __name__ == '__main__':
    main()