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
MOD998244353 = 998244353
MOD1000000007 = 1000000007

class SegmentTree:
    """
    https://qiita.com/takayg1/items/b7b3f7d458915bcc7a4e
    """
    def __init__(self, iter: Iterator, ele: Any) -> None:
        """
        iter: Iterator(初期化対象)
        func: 評価関数
        ele: 単位元(モノイドの単位元)
        """
        N = len(iter)
        self.ele = ele
        self.length = 1 << (N - 1).bit_length()
        self.tree = [[ele, i] for i in range(2*self.length)]

        for i in range(N):
            self.tree[self.length + i] = [iter[i], i]
        for i in range(self.length-1, 0, -1):
            self.tree[i] = self._exp(self.tree[2*i], self.tree[2*i + 1])

    def add(self, index: int, value: Any) -> None:
        """
        index: 更新対象
        value: 更新値
        index(0-index)の値にvalueを加算する
        """
        index += self.length
        self.tree[index][0] += value
        while index > 1:
            self.tree[index >> 1] = self._exp(self.tree[index], self.tree[index ^ 1])
            index >>= 1

    def _exp(self, f1: List[int], f2: List[int]) -> List[int]:
        if f1[0] < f2[0]:
            return f1
        else:
            return f2

    def get(self, l, r):
        """
        [l, r)の区間の値に関して
        self.funcで評価を行いO(logN)で返す
        """
        res = [self.ele, -1]

        l += self.length
        r += self.length
        while l < r:
            if l & 1:
                res = self._exp(res, self.tree[l])
                l += 1
            if r & 1:
                res = self._exp(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

#main
def main():
    # intput
    N = int(input())
    X = list(map(lambda x: int(x)-1, input().split()))
    C = list(map(int, input().split()))
    
    res = 0
    contribute = SegmentTree([0]*N, INF)
    for i in range(N):
        x, c = X[i], C[i]
        contribute.add(x, c)
    
    pushed = set()
    for i in range(N):
        cost, idx = contribute.get(0, N)
        res += cost
        if idx not in pushed:
            contribute.add(X[idx], -C[idx])
        contribute.add(idx, 2e18)
        pushed.add(idx)
    print(res)

if __name__ == '__main__':
    main()