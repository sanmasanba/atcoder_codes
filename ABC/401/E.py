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

class UnionFind():
    """
    UnionFind

    Note:
        (参考) https://note.nkmk.me/python-union-find/
    """
    def __init__(self, n: int) -> None:
        """
        UnionFind

        Args:
            n (int): 頂点の数
        """
        self.n = n
        self.parents = [-1] * n
        
    def find(self, x: int) -> int:
        """
        要素xを含む集合の根を返す
        
        Args:
            x (int): 要素x
        
        Returns:
            int: 要素xを含む集合の根
        """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x: int, y: int) -> None:
        """
        要素xが属するグループと要素yが属するグループを併合する
        
        Args:
            x (int): 要素x
            y (int): 要素y
        """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x: int) -> int:
        """
        要素xが属するグループのサイズを返す

        Args:
            x (int): 要素x

        Returns:
            int: 要素xを含む集合の要素の数
        """
        return -self.parents[self.find(x)]
    
    def same(self, x: int, y: int) -> bool:
        """
        要素xと要素yが同じグループに属するかを返す

        Args:
            x (int): 要素x
            y (int): 要素y

        Returns:
            bool: xとyが同じ集合に属するときにTrue、含まれないときにFalse
        """
        return self.find(x) == self.find(y)
    
    def members(self, x: int) -> List[int]:
        """
        要素xが属するグループに属する要素をリストで返す

        Args:
            x (int): 要素x
        
        Returns:
            List[int]: 要素xが含まれる集合の全要素のリスト
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    def roots(self) -> List[int]:
        """
        根のリストを返す
        
        Returns:
            List[int]: 根のリスト
        """
        return [i for i, x in enumerate(self.parents) if x < 0]
    
    def group_count(self) -> int:
        """
        グループの数を返す

        Returns:
            int: 現在の集合の数
        """
        return len(self.roots())
    
    def all_group_members(self) -> Dict[int, List[int]]:
        """
        {根:[そのグループに含まれる要素のリスト], ...}のdefaultdictを返す

        Returns:
            Dict[list] : 根:[要素集合]の形で記述された、全ての集合のリスト
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self) -> str:
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

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

#main
def main():
    # intput
    N, M = map(int, input().split())
    edges = []
    more_edges = defaultdict(list)
    for i in range(M):
        (u, v) = tuple(map(lambda x: int(x)-1, input().split()))
        more_edges[u].append(v)
        edges.append((u, v))
    edges = deque(sorted(edges, key=lambda x: (x[1], x[0])))
    
    uf = UnionFind(N)
    memo = SegmentTree([0]*N, seg_func, 0)
    can_reach = 0
    for i in range(N):
        # i以下の頂点同士からなる辺を全て連結
        while edges and edges[0][1] <= i:
            (u, v) = edges.popleft()
            uf.union(u, v)
        
        # i以下の頂点が全て0と連結であるか
        # iは0にして,それに連結iより大きい成分を1とする
        while can_reach <= i:
            if uf.same(0, can_reach):
                memo.update(can_reach, 0)
                for j in more_edges[can_reach]:
                    memo.update(j, 1)
                can_reach += 1
            else:
                break
        # 到達可能なら合計、不能なら-1
        if can_reach-1 == i:
            # print(uf.members(0), memo.get(0, N), memo.tree[memo.length:memo.length+N])
            print(memo.get(0, N))
        else:
            # print(uf.members(0), -1)
            print(-1)
            continue

if __name__ == '__main__':
    main()