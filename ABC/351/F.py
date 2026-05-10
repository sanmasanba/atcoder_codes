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
    return x + y

def position_compress(X):
    A = sorted(list(set(X)))
    o2c = {a:i for i, a in enumerate(A)}
    return o2c

#main
def main():
    # intput
    N = int(input())
    A = list(map(int, input().split()))

    # 座標圧縮をする
    o2c = position_compress(A)

    # 自身より小さい要素に対して、総和を求めて引く
    memo = SegmentTree([0]*(4*10**5+10), seg_func, 0)
    cnt = SegmentTree([0]*(4*10**5+10), seg_func, 0)
    memo.add(o2c[A[0]], A[0])
    cnt.add(o2c[A[0]], 1)
    res = 0
    for j in range(1, N):
        Aj = A[j]
        sum_Ai = memo.get(0, o2c[Aj]+1)
        cnt_Ai = cnt.get(0, o2c[Aj]+1)
        res += cnt_Ai*Aj - sum_Ai
        memo.add(o2c[Aj], Aj)
        cnt.add(o2c[Aj], 1)
    print(res)

if __name__ == '__main__':
    main()