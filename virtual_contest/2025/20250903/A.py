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
    N, M = map(int, input().split())
    
    nmemo = [0]*61
    b = 1
    for i in range(61):
        n = N//b
        t = n//2
        nmemo[i] = t * b + max(0, (N%(2*b)+1)-b)
        b *= 2
    res = 0
    for i in range(61):
        if (M >> i) & 1:
            res  = (res + nmemo[i]) % MOD998
    
    print(res)

if __name__ == '__main__':
    main()