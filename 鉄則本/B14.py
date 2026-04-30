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
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    if N == 1:
        if A[0] == K: print('Yes')
        else: print('No')
        return

    s = set([0])
    for mask in range(2**(N//2)):
        tmp = 0
        for i in range(N//2):
            if mask >> i & 1:
                tmp += A[i]
        if tmp == K:
            print('Yes')
            return
        s.add(tmp)

    for mask in range(2**(N-N//2)):
        tmp = 0
        for i in range(N-N//2):
            if mask >> i & 1:
                tmp += A[N//2+i]
        if K-tmp in s:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()