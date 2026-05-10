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

class SegmentTreeWithLazyAdd:
    def __init__(self, iter: Iterable, func: Callable[..., int], ele: Any) -> None:
        """
        iter: Iterator(初期化対象)
        func: 評価関数
        ele: 単位元(モノイドの単位元)
        イテレータを受け取って、セグ木を構築する
        """
        N = len(iter)
        self.func = func
        self.ele = ele
        self.length = 1 << (N - 1).bit_length()
        self.tree = [ele] * (2 * self.length)
        self.lazy = [0] * (2 * self.length)
        for i in range(N):
            self.tree[self.length + i] = iter[i]
        for i in range(self.length - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def gindex(self, l: int, r: int):
        """
        末尾の0の数を数えることで、伝搬される区間を列挙する
        [l, r) : 更新対象
        """
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
        """
        伝搬処理
        """
        for i in reversed(ids):
            v = self.lazy[i]
            if v == 0:
                continue
            self.lazy[i] = 0
            self.lazy[2 * i] += v
            self.lazy[2 * i + 1] += v
            self.tree[2 * i] += v
            self.tree[2 * i + 1] += v

    def add(self, l: int, r: int, x: Any) -> None:
        """
        [l, r): 更新対象(0-index)
        value: 更新値
        [l ,r)の値にvalueを加算する
        """
        idx = self.gindex(l, r)
        l += self.length
        r += self.length
        while l < r:
            if l & 1:
                self.lazy[l] += x
                self.tree[l] += x
                l += 1
            if r & 1:
                self.lazy[r - 1] += x
                self.tree[r - 1] += x
            r >>= 1
            l >>= 1
        for i in idx:
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def get(self, l: int, r: int):
        """
        [l, r)の区間の値に関して
        self.funcで評価を行いO(logN)で返す
        """
        self.propagate(*self.gindex(l, r))

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

def seg_func(x, y):
    return x + y

#main
def main():
    # intput
    N = int(input())
    A = list(map(int, input().split()))
    
    B = SegmentTreeWithLazyAdd(A, seg_func, 0)
    for i in range(N-1):
        stones = B.get(i, i+1)
        if stones == 0:
            continue
        # add
        B.add(i+1, min(i+stones+1, N), 1)
        # sub
        b = min(N, i+stones+1)-i-1
        B.add(i, i+1, -b)

    for i in range(N):
        print(B.get(i, i+1), end=' ')

if __name__ == '__main__':
    main()