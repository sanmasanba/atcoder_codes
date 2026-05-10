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

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(key=lambda x: abs(x))
    if N <= 2:
        print('Yes')
    elif all(abs(A[0])==abs(a) for a in A):
        mi, ma = 0, 0
        for a in A:
            if a < 0: mi += 1
            else: ma += 1
        if abs(mi-ma) <= 1 or mi == 0 or ma == 0:
            print('Yes')
        else:
            print('No')
    else:
        for i in range(1, N-1):
            if A[i]*A[i] != A[i-1]*A[i+1]:
                print('No')
                return
        print('Yes')
        return

#main
def main():
    # intput
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()