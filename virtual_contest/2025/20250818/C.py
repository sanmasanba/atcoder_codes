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

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    memo = defaultdict(list)
    for i in range(2*N-1):
        tmp = tuple(sorted([A[i], A[i+1]]))
        if A[i] != A[i+1]: memo[tmp].append(i)
    res = 0
    for k, v in memo.items(): 
        if len(v) < 2: continue

        for i, j in combinations(v, 2):
            if i+1 == j: continue
            if i+2 == j and A[i+1] == A[j]: continue
            res += 1
    print(res)

# main
def main():
    # intput
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()