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
    N, M = map(int, input().split())
    wall = [0]*(N+1)
    for _ in range(M):
        l, r = map(lambda x: int(x)-1, input().split())
        wall[l], wall[r+1] = wall[l]+1, wall[r+1]-1
    cumsum = [0] + list(accumulate(wall))
    print(min(cumsum[1:-1]))

if __name__ == '__main__':
    main()