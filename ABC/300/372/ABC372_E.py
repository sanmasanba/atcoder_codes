#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, List, Tuple, Dict, TypeVar, Optional
T = TypeVar('T')
class UnionFind():
    ###
    #
    # UnionFindの実装
    # https://note.nkmk.me/python-union-find/
    #
    ###
    def __init__(self, n: int) -> None:
        self.n = n
        self.parents = [-1] * n
        # 各頂点の持つ要素を管理
        self.member = [[i] for i in range(n)]
    # 要素xが属するグループの根を返す
    def find(self, x: int) -> int:
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    # 要素xが属するグループと要素yが属するグループを併合する
    def union(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        # 要素数を結合
        self.parents[x] += self.parents[y]
        # yの集合の親をxとしておく
        self.parents[y] = x

        # 集合を結合する
        self.member[x] += self.member[y]
        # 上位10のみだけ保持してソート
        self.member[x] = sorted(self.member[x], reverse=True)[:10]


    # 要素xが属するグループのサイズを返す
    def size(self, x: int) -> int:
        return -self.parents[self.find(x)]
    # 要素xと要素yが同じグループに属するかを返す
    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    # 要素xが属するグループに属する要素をリストで返す
    def members(self, x: int) -> List[int]:
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    # 根のリストを返す
    def roots(self) -> List[int]:
        return [i for i, x in enumerate(self.parents) if x < 0]
    # グループの数を返す
    def group_count(self) -> int:
        return len(self.roots())
    # {根:[そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
    def all_group_members(self) -> Dict[int, List[int]]:
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    def __str__(self) -> str:
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
    
sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, Q = map(int, input().split(' '))
    uf = UnionFind(N+1)
    for _ in range(Q):
        query = list(map(int, input().split(' ')))
        match query[0]:
            case 1:
                _, u, v = query
                uf.union(u, v)
            case 2:
                _, u, k = query
                u = uf.find(u)
                members = uf.member[u]
                if len(members) < k:
                    print(-1)
                else:
                    print(members[k-1])

if __name__ == '__main__':
    main()