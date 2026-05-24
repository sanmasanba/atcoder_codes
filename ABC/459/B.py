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
    N = int(input())
    S = list(input().strip().split())
    
    res = ''
    for s in S:
        if s[0] in ('a', 'b', 'c'):
            res += '2'
        elif s[0] in ('d', 'e', 'f'):
            res += '3'
        elif s[0] in ('g', 'h', 'i'):
            res += '4'
        elif s[0] in ('j', 'k', 'l'):
            res += '5'
        elif s[0] in ('m', 'n', 'o'):
            res += '6'
        elif s[0] in ('p', 'q', 'r', 's'):
            res += '7'
        elif s[0] in ('t', 'u', 'v'):
            res += '8'
        else:
            res += '9'
    print(res)

if __name__ == '__main__':
    main()