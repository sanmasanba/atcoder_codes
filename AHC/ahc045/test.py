from collections import defaultdict
from typing import List, Dict
from itertools import combinations
import math
from math import sqrt
import sys
import random

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

def dist(ix, iy, jx, jy):
    return int(sqrt((ix-jx)*(ix-jx) + (iy-jy)*(iy-jy)))

DEBUG = 1

# read input
N, M, Q, L, W = map(int, input().split())
G = list(map(int, input().split()))
lx, rx, ly, ry = [], [], [], []
for i in range(N):
    a, b, c, d = map(int, input().split())
    lx.append(a)
    rx.append(b)
    ly.append(c)
    ry.append(d)

if DEBUG == 1:
    TRUE_POS = [list(map(int, input().split())) for _ in range(N)]

def testee(l, c):
    def _dist(a, b):
        xa, ya = TRUE_POS[a-1]
        xb, yb = TRUE_POS[b-1]
        return int(sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb)))

    uf = UnionFind(l)
    n2i = {n: i for i, n in enumerate(c)}
    E = sorted([(_dist(a, b), min(a, b), max(a, b)) for a, b in combinations(c, 2)])
    res = []
    for e in E:
        (_, u, v) = e
        if not uf.same(n2i[u], n2i[v]):
            res.append((u, v))
            uf.union(n2i[u], n2i[v])
    res.sort()
    return res

# use center of rectangle
x = [(l + r) // 2 for l, r in zip(lx, rx)]
y = [(l + r) // 2 for l, r in zip(ly, ry)]

res = [0] * M
used = [0] * N
G_sorted = [(g_size, i) for i, g_size in enumerate(G)]
G_sorted.sort(reverse=True)
sampling = random.sample(range(N), N)
for (g_size, m) in G_sorted:
    for i in sampling:
        if not used[i]:
            si = i
            break
    sum_x, sum_y = x[si], y[si]
    tx, ty, ti = 0, 0, 0
    tmp = [si]
    used[si] = 1
    for _ in range(g_size-1):
        min_dist = 1 << 30
        for j in range(N):
            if used[j]:
                continue
            crr_dist = dist(sum_x/len(tmp), sum_y/len(tmp), x[j], y[j])
            if crr_dist < min_dist:
                tx, ty, ti = x[j], y[j], j
                min_dist = crr_dist
        tmp.append(ti)
        used[ti] = 1
        sum_x, sum_y = sum_x + tx, sum_y + ty
    res[m] = tmp

def kruskal(points):
    uf = UnionFind(len(points))
    n2i = {n: i for i, n in enumerate(points)}
    dists = [(dist(x[u], y[u], x[v], y[v]), u, v) for u, v in combinations(points, 2)]
    dists.sort()
    res = []
    for _, u, v in dists:
        if not uf.same(n2i[u], n2i[v]):
            res.append((u, v))
            uf.union(n2i[u], n2i[v])
    return res

print('!')
for i, v in enumerate(res):
    assert G[i] == len(v)
    print(*v, flush=True)
    if 1 < len(v):
        e = kruskal(v)
        for (u, v) in e:
            print(u, v, flush=True)
