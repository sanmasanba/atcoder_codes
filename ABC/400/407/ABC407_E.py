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

def solver(N: int, A: list):
    res = 0
    stack = []
    for i, a in enumerate(A, start=1):
        if not stack:
            stack.append(a)
            continue

        if stack[-1] <= a and len(stack) < 2*N-i:
            stack.append(a)
        else:
            res += stack.pop()
    return res

#main
def main():
    # intput
    T = int(input())

    for _ in range(T):
        N = int(input())
        A = list(int(input()) for _ in range(2*N))
        print(solver(N, A))

if __name__ == '__main__':
    main()