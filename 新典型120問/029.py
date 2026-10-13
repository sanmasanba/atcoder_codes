# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, isqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, NamedTuple, \
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


def bfs(G, removed, s, g):
    queue = deque([s])
    prev_n = {s: None}
    prev_e = {}
    while queue:
        cur = queue.popleft()
        if cur == g:
            break
        for nxt, idx in G[cur]:
            if not removed[nxt] and nxt not in prev_n:
                prev_n[nxt] = cur
                prev_e[nxt] = idx
                queue.append(nxt)

    ret = []
    cur = g
    while cur != s:
        pn = prev_n[cur]
        ret.append((pn, cur, prev_e[cur]))
        cur = pn
    return ret[::-1]

# main
def main():
    # intput
    N = int(input())
    P = list(map(lambda x: int(x)-1, input().split()))
    M = int(input())
    uf = UnionFind(N)

    G = [[] for _ in range(N)]
    deg = [0]*N
    for i in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        # すでに移動可能ならその辺はいらない
        if not uf.same(a, b):
            G[a].append((b, i))
            G[b].append((a, i))
            uf.union(a, b)
            deg[a] += 1
            deg[b] += 1

    # 1) 頂点 i と Pi が同じ連結成分にないとき、移動不可
    for i in range(N):
        if not uf.same(i, P[i]):
            print(-1)
            return

    # 逆引き
    pos = [0] * N
    for i, p in enumerate(P):
        pos[p] = i

    # 葉から確定させる
    q = deque([i for i in range(N) if deg[i] <= 1])
    removed = [False] * N
    res = []
    
    while q:
        u = q.popleft()
        # 2-1) 削除済みならスルー
        if removed[u]:
            continue

        # 2-2) bfsを使って使う辺を探索する
        cur = pos[u]
        if cur != u:
            tmp = bfs(G, removed, cur, u)

            # 返されたノードからシミュレート
            for x, y, idx in tmp:
                vx, vy = P[x], P[y]
                P[x], P[y] = P[y], P[x]
                pos[vx], pos[vy] = y, x
                res.append(idx + 1)

        # 2-3) 確定した頂点を使わないようにする
        removed[u] = True
        for nxt, _ in G[u]:
            if not removed[nxt]:
                deg[nxt] -= 1
                if deg[nxt] <= 1:
                    q.append(nxt)

    print(len(res))
    print(*res)

if __name__ == '__main__':
    main()
