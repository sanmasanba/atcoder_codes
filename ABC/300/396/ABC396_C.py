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
    N, M = map(int, input().split())
    B = list(map(int, input().split()))
    W = list(map(int, input().split()))
    B.sort(reverse=True)
    W.sort(reverse=True)

    cumsumB = [0] + list(accumulate(B))
    cumsumW = [0] + list(accumulate(W))
    tmpW = []
    tmpmax = -1e-10
    for w in cumsumW:
        tmpmax = max(tmpmax, w)
        tmpW.append(tmpmax)
    
    res = 0
    for i in range(N+1):
        res = max(res, cumsumB[i] + tmpW[min(i, len(tmpW)-1)])
    print(res)

if __name__ == '__main__':
    main()