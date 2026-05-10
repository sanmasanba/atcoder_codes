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
    T = int(input())
    res = []
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        _res = 0
        candidate = defaultdict(list)
        for i in range((2*N)-1):
            a, b = min(A[i], A[i+1]), max(A[i], A[i+1])
            if a != b:
                candidate[(a, b)].append(i)
        for _, v in candidate.items():
            if 2 <= len(v):
                for i, j in combinations(v, 2):
                    # [1 2 1 3] のようなパターンをはじく
                    if i + 1 == j:
                        continue
                    # [1 2 2 1] のようなパターンをはじく
                    if i + 2 == j and A[i+1] == A[j]:
                        continue    
                    _res += 1
        res.append(_res)
    print(*res, sep='\n')

if __name__ == '__main__':
    main()