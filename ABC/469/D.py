# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
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

# main
def main():
    # intput
    N, M = map(int, input().split())
    A, B = zip(*[list(map(int, input().split())) for _ in range(M)])

    # 1) M == 1 なら A0, B0 のいずれかがあればいい
    if M == 1:
        print(2*N - 3)
        return

    # 2) 以下の4組のみ許される
    res = set()
    if A[0] != A[1]: res.add(((min(A[0], A[1]), max(A[0], A[1]))))
    if A[0] != B[1]: res.add(((min(A[0], B[1]), max(A[0], B[1]))))
    if B[0] != A[1]: res.add(((min(B[0], A[1]), max(B[0], A[1]))))
    if B[0] != B[1]: res.add(((min(B[0], B[1]), max(B[0], B[1]))))

    # 3) 許可された組合わせに対して全部調べる
    for i in range(M):
        cand = (A[i], B[i])
        tmp = set()
        for (x, y) in list(res):
            if x in cand or y in cand:
                tmp.add((x, y))
        res = tmp

    # 4) 全てにA0, B0 がふくまれるなら足してく
    if all(A[0] == A[i] or A[0] == B[i] for i in range(M)):
        for i in range(1, N+1):
            if A[0] != i: res.add(((min(A[0], i), max(A[0], i))))
    if all(B[0] == A[i] or B[0] == B[i] for i in range(M)):
        for i in range(1, N+1):
            if B[0] != i: res.add(((min(B[0], i), max(B[0], i))))
    
    print(len(res))

if __name__ == '__main__':
    main()