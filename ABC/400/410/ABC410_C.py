#library
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

#main
def main():
    # intput
    N, Q = map(int, input().split())
    A = [i+1 for i in range(N)]

    bias = 0
    for q in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            A[(q[1]-1+bias)%N] = q[2]
        elif q[0] == 2:
            print(A[(q[1]-1+bias)%N])
        elif q[0] == 3:
            bias += q[1]

if __name__ == '__main__':
    main()