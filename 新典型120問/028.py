# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, isqrt, pi, gcd, lcm, factorial
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

class UnionFind():
    def __init__(self, n: int) -> None:
        self.n = n
        # i 以上で最初に空いている要素
        self.parents = list(range(n))
        
    def find(self, x: int) -> int:
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def update(self, x: int) -> None:
        # x が埋まったら、x の空きマスを隣の空きマスにする
        self.parents[x] = self.find((x + 1) % len(self.parents))


# main
def main():
    # intput
    Q = int(input())
    N = 2**20
    uf = UnionFind(N)

    res = [-1]*N
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = uf.find(x%N)
            res[h] = x
            uf.update(h)
        else:
            print(res[x%N])

if __name__ == '__main__':
    main()
