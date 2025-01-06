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

import math

class SortedSet(Generic[T]):
    #
    # https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
    #
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24
    
    def __init__(self, a: Iterable[T] = []) -> None:
        # Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)
        a = list(a)
        n = len(a)
        if any(a[i] > a[i + 1] for i in range(n - 1)):
            a.sort()
        if any(a[i] >= a[i + 1] for i in range(n - 1)):
            a, b = [], a
            for x in b:
                if not a or a[-1] != x:
                    a.append(x)
        n = self.size = len(a)
        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
        self.a = [a[n * i // num_bucket : n * (i + 1) // num_bucket] for i in range(num_bucket)]

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j
    
    def __eq__(self, other) -> bool:
        return list(self) == list(other)
    
    def __len__(self) -> int:
        return self.size
    
    def __repr__(self) -> str:
        return 'SortedSet' + str(self.a)
    
    def __str__(self) -> str:
        s = str(list(self))
        return '{' + s[1 : len(s) - 1] + '}'

    def _position(self, x: T) -> Tuple[List[T], int, int]:
        # return the bucket, index of the bucket and position in which x should be. self must not be empty.
        for i, a in enumerate(self.a):
            if x <= a[-1]: break
        return (a, i, bisect_left(a, x))

    def __contains__(self, x: T) -> bool:
        if self.size == 0: return False
        a, _, i = self._position(x)
        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        # Add an element and return True if added. / O(√N)
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a, b, i = self._position(x)
        if i != len(a) and a[i] == x: return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b:b+1] = [a[:mid], a[mid:]]
        return True
    
    def _pop(self, a: List[T], b: int, i: int) -> T:
        ans = a.pop(i)
        self.size -= 1
        if not a: del self.a[b]
        return ans

    def discard(self, x: T) -> bool:
        # Remove an element and return True if removed. / O(√N)
        if self.size == 0: return False
        a, b, i = self._position(x)
        if i == len(a) or a[i] != x: return False
        self._pop(a, b, i)
        return True
    
    def lt(self, x: T) -> Optional[T]:
        # Find the largest element < x, or None if it doesn't exist.
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]
    def le(self, x: T) -> Optional[T]:
        # Find the largest element <= x, or None if it doesn't exist.
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Optional[T]:
        # Find the smallest element > x, or None if it doesn't exist.
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Optional[T]:
        # Find the smallest element >= x, or None if it doesn't exist.
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]
    
    def __getitem__(self, i: int) -> T:
        # Return the i-th element.
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0: return a[i]
        else:
            for a in self.a:
                if i < len(a): return a[i]
                i -= len(a)
        raise IndexError
    
    def pop(self, i: int = -1) -> T:
        # Pop and return the i-th element.
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0: return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self.a):
                if i < len(a): return self._pop(a, b, i)
                i -= len(a)
        raise IndexError
    
    def index(self, x: T) -> int:
        # Count the number of elements < x.
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        # Count the number of elements <= x.
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans

#main
def main():
    # intput
    N, M, Sx, Sy = map(int, input().split())
    X, Y = zip(*[list(map(int, input().split())) for _ in range(N)])
    D, C = [], []
    for _ in range(M):
        d, c = input().split()
        D.append(d)
        C.append(int(c))
    
    X_set = {}
    Y_set = {}
    for x, y in zip(X, Y):
        if x not in X_set:
            X_set[x] = SortedSet()
        X_set[x].add(y)
        if y not in Y_set:
            Y_set[y] = SortedSet()
        Y_set[y].add(x)
        
    move2d = {'U':0, 'D':1, 'L':2, 'R':3}
    d = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    px, py = Sx, Sy
    res = set()
    for ds, c in zip(D, C):
        dx, dy = d[move2d[ds]]
        nx, ny = px+dx*c, py+dy*c
        if ds in ('D', 'U'):
            if px in X_set:
                lower = X_set[px].index(min(py, ny))
                upper = X_set[px].index_right(max(py, ny))
                tmp = []
                if lower < upper:
                    ys = []
                    for i in range(lower, upper):
                        y = X_set[px][i]
                        ys.append(y)
                    for y in ys:
                        X_set[px].discard(y)
                        res.add((px, y))
                        tmp.append((px, y))
                for x, y in tmp:
                    Y_set[y].discard(x)
        elif ds in ('L', 'R'):
            if py in Y_set:
                lower = Y_set[py].index(min(px, nx))
                upper = Y_set[py].index_right(max(px, nx))
                tmp = []
                if lower < upper:
                    xs = []
                    for i in range(lower, upper):
                        x = Y_set[py][i]
                        xs.append(x)
                    for x in xs:    
                        Y_set[py].discard(x)
                        res.add((x, py))
                        tmp.append((x, py))
                for x, y in tmp:
                    X_set[x].discard(y)
        px, py = nx, ny
    
    print(px, py, len(res))

if __name__ == '__main__':
    main()