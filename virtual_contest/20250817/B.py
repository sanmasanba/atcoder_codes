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

# 258_C
# main
def main():
    # intput
    N, Q = map(int, input().split())
    S = list(input().strip())
    cursor = 0
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            if cursor - query[1] < 0: 
                cursor = N - query[1] + cursor
            else:
                cursor -= query[1]
        elif query[0] == 2:
            print(S[(cursor+query[1]-1)%N])

if __name__ == '__main__':
    main()