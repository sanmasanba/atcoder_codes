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
import math

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

def is_out_of_range(x:int, y:int, Xmi:int, Xma:int, Ymi:int, Yma:int) -> bool:
    if Xmi <= x < Xma and Ymi <= y < Yma:
        return False
    else:
        return True

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    H, W = map(int, input().split(' '))
    uf = UnionFind(H*W)
    hashmap = [[W*h+w for w in range(W)] for h in range(H)]
    opened = set()

    Q = int(input())
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for _ in range(Q):
        input_ = list(map(lambda x: int(x)-1, input().split(' ')))
        match input_[0]:
            case 0:
                _, r, c = input_
                opened.add((r, c))
                for dr, dc in d:
                    nxtr, nxtc = r+dr, c+dc
                    if is_out_of_range(nxtr, nxtc, 0, H, 0, W):
                        continue
                    if (nxtr, nxtc) in opened:
                        uf.union(hashmap[r][c], hashmap[nxtr][nxtc])
            case 1:
                _, ra, ca, rb, cb = input_
                res = False
                if (ra, ca) in opened and (rb, cb) in opened:
                    res = uf.find(hashmap[ra][ca]) == uf.find(hashmap[rb][cb])
                print('Yes' if res else 'No')

if __name__ == '__main__':
    main()