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

sys.setrecursionlimit(10**6)
INF = float('inf')

def euclidean_distance(x1: T, x2: T, y1: T, y2: T) -> T:
    return (x2-x1)**2 + (y2-y1)**2

#main
def main():
    # intput
    N = int(input())
    sx, sy, tx, ty = map(int, input().split(' '))
    circles = [(list(map(int, input().split(' '))), i) for i in range(N)]

    def check(x, y):
        for circle in circles:
            tmp, i = circle
            xx, yy, rr = tmp

            if (x-xx)**2 + (y-yy)**2 - rr**2 == 0:
                return i

    # 始まりと終わりの円がどれかを調べる
    start_circle = check(sx, sy)
    target_circle = check(tx, ty)

    # グラフの構築
    uf = UnionFind(N)
    for combi in combinations(circles, 2):
        circle1, circle2 = combi
        d = euclidean_distance(circle1[0][0], circle2[0][0], circle1[0][1], circle2[0][1])
        # d < |r1 - r2|
        if d < abs(circle1[0][2] - circle2[0][2])**2:
            continue
        # d < (r1 + r2)**2
        elif d > (circle1[0][2] + circle2[0][2])**2: 
            continue
        else:
            uf.union(circle1[1], circle2[1])

    # 同じ根を持つなら移動可能
    print('Yes' if uf.same(start_circle, target_circle) else 'No')

if __name__ == '__main__':
    main()