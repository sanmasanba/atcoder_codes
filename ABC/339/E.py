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
            self.tree[i] = self.func([self.tree[2*i], self.tree[2*i + 1]])

    def update(self, index: int, value: Any) -> None:
        """
        index: 更新対象
        value: 更新値
        index(0-index)の値をvalueに更新する
        """
        index += self.length
        self.tree[index] = value
        while index > 1:
            self.tree[index >> 1] = self.func([self.tree[index], self.tree[index ^ 1]])
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
            self.tree[index >> 1] = self.func([self.tree[index], self.tree[index ^ 1]])
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
                res = self.func([res, self.tree[l]])
                l += 1
            if r & 1:
                res = self.func([res, self.tree[r - 1]])
            l >>= 1
            r >>= 1
        return res

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    # intput
    N, D = map(int, input().split())
    A = list(map(int, input().split()))
    
    # dp[i][j] := A_iまでを処理したときに末尾をjとした場合の最長の部分列
    # -> 二次元配列だと、N*Dで間に合わなくなってしまう
    # -> jの近傍以外はほとんど変化しないことに注目する
    
    # dp[j] := 末尾の文字をjとしたときに条件を満たす最長の部分列の長さ
    # -> [j-D, j+D)の範囲で、最大の長さを探して+1がjを末尾とした最長部分列
    tree_length = 500010
    seg = SegmentTree([0]*tree_length, max, -INF)
    for a in A:
        # 範囲[a-D, a+D)について
        l = max(0, a-D)
        r = min(tree_length-1, a+D)
        # 最長の長さを求める
        mx = seg.get(l, r+1)
        # 末尾をaとして
        seg.update(a, mx+1)
    
    print(seg.get(0, tree_length))

if __name__ == '__main__':
    main()