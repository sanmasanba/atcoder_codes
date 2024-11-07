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
        for i in range(self.length - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

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

#main
def main():
    # intput
    W, N = map(int, input().split(' '))
    L, R, V = [0]*(N+1), [0]*(N+1), [0]*(N+1)
    tmp_sum = 0
    for i in range(1, N+1):
        L[i], R[i], V[i] = map(int, input().split())
    
    # dp[i][j] := i個めまでで、香辛料jg使った時の価値の最大値
    dp = [[-INF] * (W+1) for _ in range(N+1)]
    dp[0][0] = 0
    segt = SegmentTree([-INF] * (W+1), max, -INF)
    segt.update(0, 0)

    for i in range(1, N+1):
        for j in range(W+1):
            dp[i][j] = dp[i-1][j]
        for j in range(W+1):
            # i番目の料理で、総量をjグラムとできる範囲
            minl = max(0, j - R[i])
            maxl = max(0, j - L[i] + 1)
            # 更新幅が0の時選ぶことができない
            if minl == maxl:
                continue
            # 範囲内で最も高いときを選ぶ
            val = segt.get(minl, maxl)
            if val != -INF:
                # jグラムにしたときの最大値で更新
                dp[i][j] = max(dp[i][j], val + V[i])
        segt = SegmentTree(dp[i], max, -INF)

    print(-1 if dp[N][W] == -INF else dp[N][W])

if __name__ == '__main__':
    main()