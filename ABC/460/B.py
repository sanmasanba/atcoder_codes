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

def solve():
    X1, Y1, R1, X2, Y2, R2 = map(int, input().split())
    if R2 > R1:
        X2, Y2, R2, X1, Y1, R1 = X1, Y1, R1, X2, Y2, R2
    
    D = (X1-X2)**2 + (Y1-Y2)**2
    if D < (R1-R2)**2 or (R1+R2)**2 < D:
        print('No')
    else:
        print('Yes')

# main
def main():
    # intput
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()