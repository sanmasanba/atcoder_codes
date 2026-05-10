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
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])  + self.lazy[i]

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
    N, M = map(int, input().split())
    S = input().strip()
    T = input().strip()
    memo = SegmentTreeWithLazyAdd([0]*N, seg_func, 0)
    for i in range(M):
        l, r = map(lambda x: int(x)-1, input().split())
        memo.add(l, r+1, 1)
    for i in range(N):
        if memo.get(i, i+1)%2==1:
            print(T[i], end='')
        else:
            print(S[i], end='')
        


if __name__ == '__main__':
    main()