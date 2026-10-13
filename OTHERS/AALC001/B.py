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

DataT = TypeVar('DataT')
LazyT = TypeVar('LazyT')

class LazySegmentTree(Generic[DataT, LazyT]):
    """
    区間作用を差し替えて使う軽量な遅延セグ木。区間は半開区間 [l, r)。
    ref: https://github.com/not522/ac-library-python/blob/master/atcoder/lazysegtree.py
    """
    def __init__(
        self,
        values: List[DataT],
        op: Callable[[DataT, DataT], DataT],
        e: DataT,
        mapping: Callable[[LazyT, DataT], DataT],
        composition: Callable[[LazyT, LazyT], LazyT],
        id_: LazyT,
    ) -> None:
        """
        values: 各要素の初期値
        op: 左右2つの区間データを結合する関数。結合律を満たす必要がある
        e: 空区間の値。opの単位元
        mapping: 作用fを区間データxに適用した結果を返す関数
        composition: 作用fをgの後に適用した合成作用を返す関数
        id_: 何もしない作用。lazyの単位元で、eとは異なることがある
        mapping(f, op(x, y)) == op(mapping(f, x), mapping(f, y)) が必要
        """
        self.n = len(values)
        self.size = 1 << (self.n - 1).bit_length() if self.n else 1
        self.log = self.size.bit_length() - 1
        self.op = op
        self.e = e
        self.mapping = mapping
        self.composition = composition
        self.id_ = id_
        self.data = [e] * (2 * self.size)
        self.lazy = [id_] * self.size
        self.data[self.size:self.size + self.n] = values
        for k in range(self.size - 1, 0, -1):
            self._update(k)

    def set(self, p: int, x: DataT) -> None:
        """p番目をxに更新する。"""
        self._push_path(p)
        k = self.size + p
        self.data[k] = x
        for i in range(1, self.log + 1):
            self._update(k >> i)

    def get(self, p: int) -> DataT:
        """p番目の値を返す。"""
        self._push_path(p)
        return self.data[self.size + p]

    def prod(self, l: int, r: int) -> DataT:
        """[l, r)の総積を返す。空区間はeを返す。"""
        if l == r:
            return self.e
        l += self.size
        r += self.size
        l0, r0 = l, r
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self._push(l >> i)
            if ((r >> i) << i) != r:
                self._push((r - 1) >> i)
        sml, smr = self.e, self.e
        while l < r:
            if l & 1:
                sml = self.op(sml, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.data[r], smr)
            l >>= 1
            r >>= 1
        for i in range(1, self.log + 1):
            if ((l0 >> i) << i) != l0:
                self._update(l0 >> i)
            if ((r0 >> i) << i) != r0:
                self._update((r0 - 1) >> i)
        return self.op(sml, smr)

    def all_prod(self) -> DataT:
        return self.data[1]

    def apply_point(self, p: int, f: LazyT) -> None:
        """p番目に作用fを適用する。"""
        self._push_path(p)
        k = self.size + p
        self.data[k] = self.mapping(f, self.data[k])
        for i in range(1, self.log + 1):
            self._update(k >> i)

    def apply(self, l: int, r: int, f: LazyT) -> None:
        """[l, r)の全要素に作用fを適用する。"""
        if l == r:
            return
        l += self.size
        r += self.size
        l0, r0 = l, r
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self._push(l >> i)
            if ((r >> i) << i) != r:
                self._push((r - 1) >> i)
        while l < r:
            if l & 1:
                self._all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self._all_apply(r, f)
            l >>= 1
            r >>= 1
        for i in range(1, self.log + 1):
            if ((l0 >> i) << i) != l0:
                self._update(l0 >> i)
            if ((r0 >> i) << i) != r0:
                self._update((r0 - 1) >> i)

    def _update(self, k: int) -> None:
        self.data[k] = self.op(self.data[2 * k], self.data[2 * k + 1])

    def _all_apply(self, k: int, f: LazyT) -> None:
        self.data[k] = self.mapping(f, self.data[k])
        if k < self.size:
            self.lazy[k] = self.composition(f, self.lazy[k])

    def _push(self, k: int) -> None:
        f = self.lazy[k]
        if f == self.id_:
            return
        self._all_apply(2 * k, f)
        self._all_apply(2 * k + 1, f)
        self.lazy[k] = self.id_

    def _push_path(self, p: int) -> None:
        for i in range(self.log, 0, -1):
            self._push((self.size + p) >> i)

# minをmaxに変える場合はseg_eも十分小さい値に変える
# S=区間min/max, F=加算値
def seg_op(a: int, b: int) -> int:
    return min(a, b)

def seg_mapping(f: int, x: int) -> int:
    return x + f

def seg_composition(f: int, g: int) -> int:
    return f + g

seg_e = 10**18
seg_id = 0

# main
def main():
    # intput
    N, Q = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    seg = LazySegmentTree(
        A,
        seg_op,
        seg_e,
        seg_mapping,
        seg_composition,
        seg_id
    )

    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            seg.apply(query[1], query[2]+1, query[3])
        elif query[0] == 2:
            print(seg.prod(query[1], query[2]+1))

if __name__ == '__main__':
    main()
