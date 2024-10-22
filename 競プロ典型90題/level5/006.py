#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, List, \
    Tuple, Dict, TypeVar, Optional, Any, Callable
from string import ascii_lowercase

T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

class SegmentTree:
    """
    """
    def __init__(self, iter: Iterator, func: Callable[..., int], ele: Any) -> None:
        """
        """
        N = len(iter)
        self.func = func
        self.ele = ele
        self.length = 1 << (N - 1).bit_length()
        self.tree = [ele] * 2*self.length

        for i in range(N):
            self.tree[self.length + i] = iter[i]
        for i in range(self.length-1, 0, -1):
            self.tree[i] = self.func(self.tree[2*i], self.tree[2*i + 1])
        
    def update(self, k: int, x: Any) -> None:
        """
        """
        k += self.length
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.func(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def get(self, l, r):
        """
        """
        res = self.ele

        l += self.length
        r += self.length
        while l < r:
            if l & 1:
                res = self.func(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.func(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

def ch_c2i(s, c2i):
    return c2i[s]

def ch_i2c(i, i2c):
    return i2c[i]

#main
def main():
    # input
    N, K = map(int, input().split(' '))
    S = list(input())
    c2i = {c:i for i, c in enumerate(ascii_lowercase)}
    i2c = {i:c for i, c in enumerate(ascii_lowercase)}
    C = list(map(lambda x:ch_c2i(x, c2i), S))
    segtree = SegmentTree(C, min, INF)

    if N == K:
        print(''.join(S))
        return

    l = 0
    res = []
    for r in range(N-K+1, N+1):
        n = segtree.get(l, r)
        res.append(n)
        while C[l] != n:
            l += 1
        l += 1
    
    # output
    res = list(map(lambda x: ch_i2c(x, i2c), res))
    print(*res, sep='')

if __name__ == '__main__':
    main()