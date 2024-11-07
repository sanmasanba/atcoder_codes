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
        self.parents[x] += self.parents[y]
        self.parents[y] = x
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

#main
def main():
    # intput
    N = int(input())
    Q = int(input())
    Asum = [None] * N
    query = []
    uf = UnionFind(N)
    for i in range(Q):
        t, x, y, v = map(lambda x:int(x)-1, input().split(' '))
        match t+1:
            case 0:
                uf.union(x, y)
                Asum[x] = v+1
            case 1:
                if uf.same(x, y):
                    query.append((x, y, v+1))
                else:
                    query.append((-1, -1, "Ambiguous"))

    A = [-1] * N
    A[0] = 0
    for i in range(N-1):
        if Asum[i] is not None:
            if A[i] == -1:
                A[i] = 0    
            A[i+1] = Asum[i] - A[i]
    
    res = []
    for x, y, v in query:
        if x == -1 and y == -1:
            res.append(v)
        else:
            d = v - A[x]
            if abs(x-y)%2:
                res.append(A[y]-d)
            else:
                res.append(A[y]+d)

    print(*res, sep='\n')

if __name__ == '__main__':
    main()