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
    def __init__(self, n: int) -> None:
        self.size = [1] * n
        self.parents = list(range(n))
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if x > y:
                x, y = y, x
            self.size[x] += self.size[y]
            self.parents[y] = x

def main():
    N, Q = map(int, input().split())
    uf = UnionFind(N+2)
    cnt = [1 for _ in range(N+2)]
    color = [i for i in range(N+2)]

    for _ in range(Q):
        input_ = list(map(int, input().split()))
        if input_[0] == 1:
            _, x, c = input_
            root = uf.find(x)
            size = uf.size[root]
            cnt[color[root]] -= size
            color[root] = c
            cnt[color[root]] += size
            if color[uf.find(root-1)] == color[root]: 
                uf.union(root-1, root)
            if color[uf.find(root+size)] == color[root]: 
                uf.union(root, root+size)
        elif input_[0] == 2:
            _, c = input_
            print(cnt[c])

if __name__ == '__main__':
    main()
