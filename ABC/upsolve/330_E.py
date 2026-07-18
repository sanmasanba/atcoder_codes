# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, NamedTuple, \
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
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    memo = defaultdict(int)
    for a in A:
        memo[a] += 1
    h = []
    for a in range(10**9+10):
        if a not in memo:
            heappush(h, a)
        # 配列に存在しない値は少なくともQ回は削除される
        if 5*10**5+10 < len(h):
            break
    
    for _ in range(Q):
        i, x = map(int, input().split())
        # 配列更新
        a, A[i-1] = A[i-1], x
        memo[a] -= 1
        memo[x] += 1    

        # 更新により要素がなくなっていれば挿入
        if memo.get(a) == 0: 
            heappush(h, a)
        while 1:
            b = heappop(h)
            if memo.get(b, 0) == 0:
                print(b)
                heappush(h, b)
                break

if __name__ == '__main__':
    main()