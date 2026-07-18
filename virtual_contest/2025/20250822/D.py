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
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    C = sorted([(a, b) for a, b in zip(A, B)])
    q = []
    res = INF
    s = 0
    for a, b in C:
        # 最大値を固定,最大値だけを消していく
        if len(q) == K-1: res = min(res, a * (s + b))
        heappush(q, -b)
        s += b
        if K <= len(q): s += heappop(q)
    print(res)

# main
def main():
    # intput
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()