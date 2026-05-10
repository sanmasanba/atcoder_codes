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

#main
def main():
    # intput
    H, W, M = map(int, input().split(' '))
    query = [list(map(int, input().split(' '))) for _ in range(M)]

    updated_r_list = SegmentTree([0]*H, sum, 0)
    updated_c_list = SegmentTree([0]*W, sum, 0)
    res = defaultdict(int)
    for T, A, X in query[::-1]:
        match T:
            case 1:
                # もしすでに更新済みなら上書きできないのでスルー
                if updated_r_list.get(A-1, A):
                    continue
                # 更新できるのは、行数 - まだ更新されていない行数
                update_cnt = W - updated_c_list.get(0, W)
                res[X] += update_cnt
                updated_r_list.update(A-1, 1)
            case 2:
                # もしすでに更新済みなら上書きできないのでスルー
                if updated_c_list.get(A-1, A):
                    continue
                # 更新できるのは、列数 - まだ更新されていない列数
                update_cnt = H - updated_r_list.get(0, H)
                res[X] += update_cnt
                updated_c_list.update(A-1, 1)
    
    keys = sorted(list(res.keys()))
    cnt0 = H*W
    ans = deque([[0, cnt0]])
    for k in keys:
        if k and res[k]:
            ans[0][1] -= res[k]
            ans.append([k, res[k]])
    
    if not ans[0][1]: ans.popleft()
    print(len(ans))
    for a in ans:
        print(*a)

if __name__ == '__main__':
    main()