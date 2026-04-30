# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

def solver():
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())), reverse=True)
    B = sorted(list(map(int, input().split())))

    c, idx = 0, 0
    for v in A:
        # s = min(f(A, B)) 
        #   = \sum(ai, bi) - M*c(cはai+biがMを超える組み合わせの数)
        while idx < N and B[idx]+v < M:
            idx += 1
        if N <= idx : break
        c +=1
        idx += 1
    print(sum(A)+sum(B)-M*c)

# main
def main():
    # intput
    T = int(input())
    for _ in range(T):
        solver()

if __name__ == '__main__':
    main()