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
MOD998244353 = 998244353
MOD1000000007 = 1000000007

def chmin(a, b):
    return min(a, b), max(a, b)

#main
def main():
    # intput
    N, M = map(int, input().split())
    res = 0
    seen = set()
    for _ in range(M):
        a, b = map(int, input().split())
        a, b = chmin(a, b)        
        if a == b or (a, b) in seen:
            res += 1
        seen.add((a, b))
    print(res)

if __name__ == '__main__':
    main()