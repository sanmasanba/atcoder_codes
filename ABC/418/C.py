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
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    CUMSUM = [0] + list(accumulate(A))
    M = A[-1]
    for _ in range(Q):
        B = int(input())
        # いずれのティーバッグより多いとき、適切に選ぶことができない
        if M < B:
            print(-1)
        elif B == 1:
            print(1)
        else:
            idx = bisect_left(A, B)
            print((N-(idx+1))*(B-1) + CUMSUM[idx] + min(B, A[idx]))

if __name__ == '__main__':
    main()