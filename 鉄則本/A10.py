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
    N = int(input())
    A = list(map(int, input().split()))
    D = int(input())
    L, R = [0]*(N+1), [0]*(N+1)
    for i in range(N):
        L[i+1] = max(A[i], L[i])
        R[N-(i+1)] = max(A[-(1+i)], R[N-i])
    res = []
    for _ in range(D):
        l, r = map(int, input().split())
        res.append(max(L[l-1], R[r]))
    print(*res, sep='\n')

if __name__ == '__main__':
    main()