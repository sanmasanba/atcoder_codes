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

#main
def main():
    # intput
    N = int(input())
    P = list(map(int, input().split()))
    res = [0] * N

    r = 1
    while 1:
        m = -1
        for p in P:
            m = max(m, p)
        if m == 0:
            break
        cnt = 0
        for i in range(N):
            if P[i] == m:
                res[i] = r
                P[i] = 0
                cnt += 1
        r += cnt
    
    for r in res:
        print(r)

if __name__ == '__main__':
    main()