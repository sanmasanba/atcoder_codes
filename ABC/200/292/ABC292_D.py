#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')
class UnionFind():
    ###
    #
    # UnionFindの実装
    #
    ###
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    def size(self, x):
        return -self.parents[self.find(x)]
    def same(self, x, y):
        return self.find(x) == self.find(y)
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

#main
def main():
    N, M = map(int, input().split(' '))
    uf = UnionFind(N)
    U, V = [], []
    # unionfindで成分を結合していく
    for _ in range(M):
        u, v = map(lambda x: int(x)-1, input().split(' '))
        U.append(u)
        V.append(v)
        uf.union(u, v)
    # 根と辺の管理
    ns = [0 for _ in range(N)]
    es = [0 for _ in range(N)]
    # 根ごとの成分の個数を数える
    for i in range(N):
        ns[uf.find(i)] += 1
    # 根ごとに、各成分が何回結合したかを求める
    for i in range(M):
        es[uf.find(U[i])] += 1
    print("Yes" if ns == es else "No")

if __name__ == '__main__':
    main()