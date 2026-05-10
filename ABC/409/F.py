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
        self.groups = n
        
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
        self.groups -= 1

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
        return self.groups
    
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

N, Q = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
querys = [list(map(lambda x: int(x)-1, input().split())) for _ in range(Q)]

def dist(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)

def make_hash(d, i, j):
    return d * (1 << 24) + i * (1 << 12) + j

def get_kij(_hash):
    mask = (1 << 12) - 1
    i = (_hash >> 12) & mask
    j = _hash & mask
    d = _hash >> 24
    return d, i, j

edges = []
for i, j in combinations(range(N), 2):
    heappush(edges, make_hash(dist(XY[i][0], XY[i][1], XY[j][0], XY[j][1]), i, j))
# 頂点は最大でもN + Q
uf = UnionFind(N+Q)

cnt = 0
for q in querys:
    if q[0] == 0:
        _, x, y = q
        # 組み合わせの追加 -> O((N+Q)log(N+Q))
        for i, (xx, yy) in enumerate(XY):
            heappush(edges, make_hash(dist(x+1, y+1, xx, yy), i, len(XY)))
        # 座標の追加
        XY.append([x+1, y+1])
        cnt += 1
    elif q[0] == 1:
        mind = -1
        if uf.group_count()-Q+cnt > 1:
            while edges:
                kij = heappop(edges)
                k, i, j = get_kij(kij)
                if not uf.same(i, j):
                    if mind == -1:
                        mind = k
                        uf.union(i, j)
                    elif mind == k:
                        uf.union(i, j)
                    else:
                        heappush(edges, kij)
                        break
        print(mind)
    elif q[0] == 2:
        _, a, b = q
        if uf.same(a, b): 
            print('Yes')
        else: 
            print('No')