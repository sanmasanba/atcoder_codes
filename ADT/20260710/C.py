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
    res = [False]*M
    memo = [-1]*N
    for i in range(M):
        a, b = input().split()
        a = int(a)-1
        if b == 'F':
            continue
        if memo[a] == -1:
            res[i] = True
            memo[a] = i
    for r in res:
        print('Yes' if r else 'No')
    
if __name__ == '__main__':
    main()