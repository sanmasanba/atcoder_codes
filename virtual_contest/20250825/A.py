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
    S = [[0]*M for _ in range(N)]
    for i in range(M):
        k, *s = map(int, input().split())
        for j in range(k):
            S[s[j]-1][i] = 1
    P = list(map(int, input().split()))

    def check(memo):
        for i, m in enumerate(memo):
            if m%2 != P[i]: return 0
        return 1

    res = 0
    for bit in range(2**N):
        memo = [0]*M
        for i in range(N):
            if (bit >> i) & 1:
                for j, s in enumerate(S[i]):
                    if s: memo[j] += 1
        res += check(memo)
    print(res)

if __name__ == '__main__':
    main()