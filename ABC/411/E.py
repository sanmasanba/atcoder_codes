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

class SegmentTreeWithLazyUpdate:
    """
    https://qiita.com/ether2420/items/7b67b2b35ad5f441d686
    """
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
        self.lazy = [None] * (2 * self.length)
        for i in range(N):
            self.tree[self.length + i] = iter[i]
        for i in range(self.length - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def gindex(self, l: int, r: int):
        """
        末尾の0の数を数えることで、伝搬される区間を列挙する
        [l ,r) : 更新対象
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
            if v is None:
                continue
            self.lazy[2 * i] = v
            self.lazy[2 * i + 1] = v
            self.tree[2 * i] = v
            self.tree[2 * i + 1] = v
            self.lazy[i] = None

    def update(self,l,r,x):
        """
        [l, r): 更新対象(0-index)
        value: 更新値
        [l ,r)の値をvalueに更新する
        """
        ids = self.gindex(l,r)
        self.propagate(*self.gindex(l,r))
        l += self.length
        r += self.length
        while l<r:
            if l&1:
                self.lazy[l] = x
                self.tree[l] = x
                l += 1
            if r&1:
                self.lazy[r-1] = x
                self.tree[r-1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = self.func(self.tree[2*i], self.tree[2*i+1])

    def get(self, l, r):
        """
        [l, r)の区間の値に関して
        self.funcで評価を行いO(logN)で返す
        """
        *idx, = self.gindex(l, r)
        self.propagate(*idx)

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
    return (x + y)%MOD998

def mod_inverse(a, p):
    return pow(a, p-2, p)

#main
def main():
    # intput
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    
    def preprocess():
        tmp = set()
        for row in A:
            for a in row:
                tmp.add(a)
        tmp = sorted(list(tmp))
        return {a:i+1 for i, a in enumerate(tmp)}

    n2n = preprocess()

    dp = SegmentTreeWithLazyUpdate([0]*(len(n2n)+10), seg_func, 0)
    dp.update(0, 1, 1)
    
    mi = -1
    for row in A:
        cnt = Counter(row)
        nums = sorted(list(cnt.keys()), reverse=True)
        for num in nums:
            sum_p = dp.get(0, n2n[num]+1)
            dp.update(n2n[num], 
                      n2n[num] + 1, 
                      (sum_p*cnt[num]%MOD998)*mod_inverse(6, MOD998)%MOD998
                      )
        mi = max(mi, min(row))
        dp.update(0, n2n[mi], 0)
            
    res = 0
    for i, v in n2n.items():
        res += i*dp.get(v, v+1)
        res %= MOD998
    print(res)

if __name__ == '__main__':
    main()