#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

from typing import Callable, Any, Iterable

class SegmentTreeWithLazyUpdate:
    def __init__(self, iter: Iterable, func: Callable[..., int], ele: Any) -> None:
        N = len(iter)
        self.func = func
        self.ele = ele
        self.length = 1 << (N - 1).bit_length()
        self.tree = [ele] * (2 * self.length)
        self.lazy = [None] * (2 * self.length)
        for i in range(N):
            self.tree[self.length + i] = iter[i]
        for i in range(self.length - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def gindex(self, l: int, r: int):
        l += self.length
        r += self.length
        lm = l >> (l & -l).bit_length()
        rm = r >> (r & -r).bit_length()

        while r > l:
            if l <= lm:
                yield l
            if r <= rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1
    
    def propagate(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[2 * i] = v
            self.lazy[2 * i + 1] = v
            self.tree[2 * i] = v
            self.tree[2 * i + 1] = v
            self.lazy[i] = None

    def update(self,l,r,x):
        ids = self.gindex(l,r)
        self.propagate(*self.gindex(l,r))
        l += self.length
        r += self.length
        while l<r:
            if l&1:
                self.lazy[l] = x
                self.tree[l] = x
                l += 1
            if r&1:
                self.lazy[r-1] = x
                self.tree[r-1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = self.func(self.tree[2*i], self.tree[2*i+1])

    def get(self, l, r):
        *idx, = self.gindex(l, r)
        self.propagate(*idx)

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

#main
def main():
    # intput
    W, N = map(int, input().split(' '))
    blocks = SegmentTreeWithLazyUpdate([0]*(5*10**5+10), max, -INF)
    
    res = []
    for _ in range(N):
        l, r = map(int, input().split(' '))
        crr_hight = blocks.get(l, r+1)
        update_height = crr_hight + 1
        res.append(update_height)
        blocks.update(l, r+1, update_height)
    
    print(*res, sep='\n')

if __name__ == '__main__':
    main()