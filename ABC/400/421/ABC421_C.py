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

# main
def main():
    # intput
    N = int(input())
    S = list(input().strip())
    
    resA, resB = 0, 0
    curA, curB = 0, 0
    for i, s in enumerate(S):
        if s == 'A':
            resA += abs(curA-i)
            curA += 2
        elif s == 'B':
            resB += abs(curB-i)
            curB += 2
    print(min(resA, resB))

if __name__ == '__main__':
    main()