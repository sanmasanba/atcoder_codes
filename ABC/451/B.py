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
    A, B = zip(*[list(map(int, input().split())) for _ in range(N)])
    cur = [0] * M
    nxt = [0] * M

    for i in range(N):
        a, b = A[i], B[i]
        cur[a-1] += 1
        nxt[b-1] += 1
    
    for a, b in zip(cur, nxt):
        print(b-a)

if __name__ == '__main__':
    main()