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
sx, sy, si = 100000, 100000, 0
for i in range(N):
    a, b, c, d = map(int, input().split())
    lx.append(a)
    rx.append(b)
    ly.append(c)
    ry.append(d)
    x, y = (a + b)//2, (c + d)//2
    if dist(0, 0, x, y) < dist(0, 0, sx, sy):
        sx, sy, si = x, y, i

if DEBUG == 1:
    TRUE_POS = [list(map(int, input().split())) for _ in range(N)]

def testee(l, c):
    def dist(a, b):
        xa, ya = TRUE_POS[a-1]
        xb, yb = TRUE_POS[b-1]
        return int(sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb)))

    uf = UnionFind(l)
    n2i = {n: i for i, n in enumerate(c)}
    E = sorted([(dist(a, b), min(a, b), max(a, b)) for a, b in combinations(c, 2)])
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

def total_distance(points):
    res = 0
    for i in range(N-1):
        u, v = points[i], points[i+1]
        xu, yu, xv, yv = x[u], y[u], x[v], y[v]
        res += dist(xu, yu, xv, yv)
    return res

# make snake graph
def make_init_route(si, sx, sy):
    used = [0]*N
    init_res = []
    for _ in range(N):
        init_res.append(si)
        used[si] = 1
        tx, ty, ti = 100000, 100000, 0
        for gi in range(N):
            if used[gi]:
                continue
            gx, gy = x[gi], y[gi]
            if dist(sx, sy, gx, gy) < dist(sx, sy, tx, ty):
                tx, ty, ti = gx, gy, gi
        sx, sy, si = tx, ty, ti
    return init_res

def simulated_annealing(points, init_temp, cooling_rate, max_iter):
    best_route = points[:]
    best_dist = total_distance(points)
    temperature = init_temp

    for _ in range(max_iter):
        i, j = sorted(random.sample(range(len(points)), 2))
        new_route = best_route[:]
        new_route[i:j+1] = reversed(new_route[i:j+1])
        new_dist = total_distance(new_route)

        perp = random.random() < math.exp(min(0.0, (best_dist - new_dist)) / temperature)
        if new_dist < best_dist or perp:
            best_dist = new_dist
            best_route = new_route

        temperature *= cooling_rate
        if temperature < 1e-3:
            break

    return best_route, best_dist

best_route = []
best_dist = 1 << 30
for si in random.choices(range(N), k=5):
    init_temp = 40
    cooling_rate = 0.97
    max_iter = 10000
    init_res = make_init_route(si=si, sx=x[si], sy=y[si])
    crr_route, crr_dist = simulated_annealing(init_res, init_temp, cooling_rate, max_iter)
    if crr_dist < best_dist:
        best_route, best_dist = crr_route, crr_dist

res = [0] * M
cursor = 0
G_sorted = [(g_size, i) for i, g_size in enumerate(G)]
G_sorted.sort(reverse=True)
for (g_size, i) in G_sorted:
    nodes = best_route[cursor: cursor+g_size]
    edges = []
    for j in range(g_size-1):
        edges.append((best_route[cursor+j], best_route[cursor+j+1]))
    res[i] = (nodes, edges)
    cursor += g_size

print('!')
for i, (v, e) in enumerate(res):
    assert G[i] == len(v)
    print(*v, flush=True)
    for (u, v) in e:
        print(u, v, flush=True)
