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

class SegmentTree:
    """
    https://qiita.com/takayg1/items/b7b3f7d458915bcc7a4e
    """
    def __init__(self, iter: Iterator, func: Callable[..., int], ele: Any) -> None:
        """
        iter: Iterator(初期化対象)
        func: 評価関数
        ele: 単位元(モノイドの単位元)
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

    def update(self, index: int, value: Any) -> None:
        """
        index: 更新対象
        value: 更新値
        index(0-index)の値をvalueに更新する
        """
        index += self.length
        self.tree[index] = value
        while index > 1:
            self.tree[index >> 1] = self.func(self.tree[index], self.tree[index ^ 1])
            index >>= 1

    def add(self, index: int, value: Any) -> None:
        """
        index: 更新対象
        value: 更新値
        index(0-index)の値にvalueを加算する
        """
        index += self.length
        self.tree[index] += value
        while index > 1:
            self.tree[index >> 1] = self.func(self.tree[index], self.tree[index ^ 1])
            index >>= 1

    def get(self, l, r):
        """
        [l, r)の区間の値に関して
        self.funcで評価を行いO(logN)で返す
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

def seg_func(x, y):
    return max(x, y)

def func(i, j):
    ai, bi = i
    aj, bj = j
    if ai > aj:
        return 1
    elif ai < aj:
        return -1
    else:
        if bi > bj:
            return -1
        elif bi < bj:
            return 1
        else: 
            return 0

def cmp(a, b):
    a_map = {n:i for i, n in enumerate(sorted(set(a)))}
    b_map = {n:i for i, n in enumerate(sorted(set(b)))}
    a_ = list(map(lambda x: a_map[x], a))
    b_ = list(map(lambda x: b_map[x], b))
    return sorted([(aa, bb) for aa, bb in zip(a_, b_)], key=cmp_to_key(func))

# main
def main():
    # intput
    N = int(input())
    A, B = zip(*[list(map(int, input().split())) for _ in range(N)])
    
    cmp_ab = cmp(A, B)
    seg = SegmentTree([0]*(N+1), seg_func, 0)

    seen = set()
    for a, b in cmp_ab:
        seg.update(b, seg.get(0, b)+1)
        seen.add(a)
    print(seg.get(0, N+1))

if __name__ == '__main__':
    main()