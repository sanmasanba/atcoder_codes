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
        self.n = N
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
            index >>= 1
            self.tree[index] = self.func(self.tree[2 * index], self.tree[2 * index + 1])

    def add(self, index: int, value: Any) -> None:
        """
        index: 更新対象
        value: 更新値
        index(0-index)の値にvalueを加算する
        """
        index += self.length
        self.tree[index] += value
        while index > 1:
            index >>= 1
            self.tree[index] = self.func(self.tree[2 * index], self.tree[2 * index + 1])

    def get(self, l, r):
        """
        [l, r)の区間の値に関して
        self.funcで評価を行いO(logN)で返す
        """
        left = right = self.ele

        l += self.length
        r += self.length
        while l < r:
            if l & 1:
                left = self.func(left, self.tree[l])
                l += 1
            if r & 1:
                right = self.func(self.tree[r - 1], right)
            l >>= 1
            r >>= 1
        return self.func(left, right)

    def max_right(self, l: int, pred: Callable[[Any], bool]) -> int:
        """
        pred(get(l, r))がTrueとなる最大のrをO(log N)で返す。
        
        Args:
            l: 探索開始位置（含む）。0 <= l <= n。nは元の配列の要素数。
            pred: 区間の集約値を受け取り、条件を満たすかをboolで返す関数。
        
        Returns:
            r（l <= r <= n）。[l, r)は条件を満たし、r < nなら[l, r + 1)は満たさない。
            [l, n)全体でTrueならn、最初の要素でFalseならl（空区間）を返す。
        
        Notes:
            pred(ele) == True。同じ値への判定結果が変わらず、副作用を持たないこと。
            lを固定してrを増やすと、判定はTrueからFalseへ変わり、Trueに戻らないこと。
        
        Examples:
            非負の区間和でseg.max_right(l, lambda s: s <= K)
        """
        assert 0 <= l <= self.n
        assert pred(self.ele)
        if l == self.n:
            return self.n
        l += self.length
        value = self.ele
        while True:
            while l % 2 == 0:
                l >>= 1
            nxt = self.func(value, self.tree[l])
            if not pred(nxt):
                while l < self.length:
                    l *= 2
                    nxt = self.func(value, self.tree[l])
                    if pred(nxt):
                        value = nxt
                        l += 1
                return l - self.length
            value = nxt
            l += 1
            if (l & -l) == l:
                return self.n

    def min_left(self, r: int, pred: Callable[[Any], bool]) -> int:
        """
        pred(get(l, r))がTrueとなる最小のlをO(log N)で返す。
        
        Args:
            r: 探索終了位置（含まない）。0 <= r <= n。nは元の配列の要素数。
            pred: 区間の集約値を受け取り、条件を満たすかをboolで返す関数。
        
        Returns:
            l（0 <= l <= r）。[l, r)は条件を満たし、l > 0なら[l - 1, r)は満たさない。
            [0, r)全体でTrueなら0、直前の要素でFalseならr（空区間）を返す。
        
        Notes:
            pred(ele) == True。同じ値への判定結果が変わらず、副作用を持たないこと。
            rを固定してlを減らすと、判定はTrueからFalseへ変わり、Trueに戻らないこと。
        
        Examples:
            非負の区間和でseg.min_left(r, lambda s: s <= K)
        """
        assert 0 <= r <= self.n
        assert pred(self.ele)
        if r == 0:
            return 0
        r += self.length
        value = self.ele
        while True:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            nxt = self.func(self.tree[r], value)
            if not pred(nxt):
                while r < self.length:
                    r = 2 * r + 1
                    nxt = self.func(self.tree[r], value)
                    if pred(nxt):
                        value = nxt
                        r -= 1
                return r + 1 - self.length
            value = nxt
            if (r & -r) == r:
                return 0

def seg_func(x, y):
    return x + y

# main
def main():
    # intput
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    seg = SegmentTree(A, seg_func, 0)

    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            _, i, x = query
            seg.update(i-1, x)
        elif query[0] == 2:
            _, l, t = query
            res = seg.max_right(l-1, lambda x: x < t)
            print(res + 1)
        elif query[0] == 3:
            _, r, t = query
            res = seg.min_left(r, lambda x: x < t)
            print(res)

if __name__ == '__main__':
    main()