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

def swap(a, b):
    return min(a, b), max(a, b)

# main
def main():
    # intput
    A, B, C, D = map(int, input().split())

    # 初期値を小さい順にswap
    a, b = swap(A, B)
    c, d = swap(C, D)

    # A < B == C < D なら二人を隣接させることなく解決できる
    if (A < B) == (C < D):
        res = abs(A - C) + abs(B - D)
    else:
        # 例: {a, b} -> {x, x+1} -> {c, d} を考える
        # 上記の例は3セクションに分解できる
        # 1) a -> x, b -> x+1
        # 2) x, x+1
        # 3) x -> c, x+1 -> d
        # 
        # よって、cost = |a - x| + |b - (x+1)| + 1 |x - c| + |x+1 - d|
        # 整理すると、cost = 1 + |a - x| + |x - (b-1)| + |x- c| + |x - (d-1)|
        # -> {a, b-1, c, d-1} に対する距離を最小化すればいい
        # -> v0, v1, v2, v3 に並び替えた時、外側と内側に分ければ、
        #    (v3 - v0) + (v2 - v1)が最小(ペアの中では値は一定)
        # -> (v3 - v0) + (v2 - v1) + 1
        v = [a, b-1, c, d-1]
        v.sort()
        res = (v[3] - v[0]) + (v[2] - v[1]) + 1

    print(res)

if __name__ == '__main__':
    main()
