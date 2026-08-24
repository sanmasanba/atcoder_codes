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
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 1) 0 から始めて、同じ場所に到達するまでシミュレート
    # このループは必ずN以内に終了する
    def solve():
        used = set()
        loop = deque()
        cnt = 0
        while cnt%N not in used:
            used.add(cnt%N)
            loop.append(cnt%N)
            cnt += A[cnt%N]
        pref = deque()
        while cnt%N != loop[0]:
            tmp = loop.popleft()
            pref.append(tmp)
        return pref, loop
    pref, loop = solve()

    # 2) pref と loop を使って圧縮して加算していく。
    # 2-1) pref は一度しかおとずれないのでそのままたしていく
    res = 0
    for idx in pref:
        K -= 1
        if K < 0:
            print(res)
            return
        res += A[idx]
    # 2-2) まとめられる分は事前に足す
    s = sum(A[idx] for idx in loop)
    M = len(loop)
    res += K//M * s
    # 2-3) 余った分を移動
    for i in range(K % M):
        res += A[loop[i]]
    print(res)

if __name__ == '__main__':
    main()
