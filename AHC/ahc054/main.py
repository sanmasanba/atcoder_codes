# library
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
import os
import random

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

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

file_name = os.path.basename(__file__)
LOCAL = file_name != 'Main.py'

N, ti, tj = map(int, input().split())
b = [list(input().strip()) for _ in range(N)]
known = [[False] * N for _ in range(N)]
known[0][N//2] = True

# 木の準備
Xtree = [SortedSet() for _ in range(N)]
Ytree = [SortedSet() for _ in range(N)]
for i in range(N):
    Xtree[i].add(-1)
    Xtree[i].add(N)
    Ytree[i].add(-1)
    Ytree[i].add(N)
    for j in range(N):
        if b[i][j] == 'T':
            Xtree[i].add(j)
            Ytree[j].add(i)

if LOCAL:
    targets = [list(map(int, input().split())) for _ in range(N**2-1)]

def retrieve(pi, pj):
    ltj, gtj = Xtree[pi].lt(pj), Xtree[pi].gt(pj)+1
    lti, gti = Ytree[pj].lt(pi), Ytree[pj].gt(pi)+1
    for j in range(max(ltj, 0), min(gtj, N)): known[pi][j] = True
    for i in range(max(lti, 0), min(gti, N)): known[i][pj] = True

def is_out_of_range(x:int, y:int, Xmi:int, Xma:int, Ymi:int, Yma:int) -> bool:
    return not (Xmi <= x < Xma and Ymi <= y < Yma)

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def check(pi, pj, ti, tj):
    # dist:vからの距離, queue:探索キュー
    dist = [[INF]*N for _ in range(N)]
    queue = deque()
    dist[ti][tj] = 0
    queue.append((ti, tj))
    while queue:
        ci, cj = queue.popleft()
        for di, dj in d:
            ni, nj = ci+di, cj+dj
            if ni == pi and nj == pj: 
                continue
            if is_out_of_range(ni, nj, 0, N, 0, N):
                continue
            if dist[ni][nj] != INF or b[ni][nj] == 'T':
                continue
            dist[ni][nj] = dist[ci][cj] + 1
            queue.append((ni, nj))
    return dist

# ローカル環境用
def move(pi, pj, flg):
    if flg:
        dist = check(pi, pj, ti, tj)
    else:
        for bi, bj in targets:
            dist = check(pi, pj, bi, bj)
            if any(dist[pi+di][pj+dj] != INF for di, dj in d if not is_out_of_range(pi+di, pj+dj, 0, N, 0, N)):
                break
    ri, rj, tmp = 0, 0, INF
    for di, dj in d:
        ni, nj = pi+di, pj+dj
        if not is_out_of_range(ni, nj, 0, N, 0, N) and dist[ni][nj] < tmp:
            ri, rj = ni, nj
            tmp = dist[ni][nj]
    return ri, rj        

def solver(pi, pj):
    dist = check(pi, pj, ti, tj)
    # ランダム配置
    tmp = [i for i in range(N**2-1)]
    random.shuffle(tmp)
    memo = []
    # for _ in range(4):
    #     tmp.extend(tmp)

    for k in tmp:
        i, j = k%N, k//N
        if (i == 0 and j == N//2) or (i == ti and j == tj) or b[i][j] == 'T':
            continue
        b[i][j] = 'T'
        dist = check(-1, N//2, ti, tj)
        if dist[0][N//2] == INF:
            b[i][j] == '.'
        else: 
            memo.append((i, j))
    print(len(memo), end=' ', flush=True)
    for m in memo: print(f"{m[0]} {m[1]}", end=' ', flush=True)
    print()

# main
def main():
    pi, pj = 0, N//2
    CAN_GOAL = False

    while True:
        # 妨害part
        # 全体を4*4(or 5*5)のグリッドに分割
        # グリッドから脱出しそうな時に妨害する発想？
        solver(pi, pj)

        # 本番環境では、座標と既知マスの情報が来る
        if not LOCAL:
            pi, pj = map(int, input().split())
            n, *xy = map(int, input().split())
        # 1. 現在位置と伝説の花を比較
        if pi == ti and pj == tj: break
        print(-1)
        return
        # 2. 現在位置から木までマスをオープン
        retrieve(pi, pj)
        # 3. 伝説の花が既知マスなら目的地に
        CAN_GOAL = known[ti][tj]

        # 4. ゴールが既知かつ到達不能ならゴールを未定に
        # TODO: 条件を守っておいたら不可侵じゃない？
        
        # 5. 目的地が未定か伝説の花以外が目的地(こんなことある？)
        # MEMO: 基本最悪を考えればいいんじゃない？

        # 6. 目的地に移動
        if LOCAL: 
            pi, pj = move(pi, pj, CAN_GOAL)

if __name__ == '__main__':
    main()
