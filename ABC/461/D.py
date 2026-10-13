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

def cumsum2d(a:List[T]) -> List[T]:
    h, w = len(a), len(a[0])
    tmp = [[0] * (w+1) for _ in range(h+1)]
    for i in range(h):
        for j in range(w):
            tmp[i+1][j+1] = (
                tmp[i+1][j]
                + tmp[i][j+1]
                - tmp[i][j]
                + a[i][j]
                )
    return tmp

# main
def main():
    # intput
    H, W, K = map(int, input().split())
    S = [list(map(int, list(input().strip()))) for _ in range(H)]
    
    c = cumsum2d(S)

    def f(r1, c1, r2, c2):
        return c[r2][c2] - c[r1][c2] - c[r2][c1] + c[r1][c1]

    res = 0
    cnt = [0] * (H*W+1)
    for hh in range(H):
        for hl in range(hh+1):
            if f(hl, 0, hh+1, W) < K:
                continue
            cnt[0] = 1
            used = [0]
            for w in range(W):
                # S0 = 0, Si = a0 + a1 + ... + a(i-1) とすると
                # 区間 [l, r) の和は
                #   al + a(l+1) + ... + a(r-1) = Sr - Sl
                #
                # これが K になる条件は
                #   Sr - Sl = K
                #   Sl = Sr - K
                #
                # よって、これまでに出現した累積和 Sl の回数をメモしておけば、
                # r を固定したときに条件を満たす l の個数がわかる
                sw = f(hl, 0, hh+1, w+1)
                res += cnt[sw - K]
                cnt[sw] += 1
                used.append(sw)

            for x in used:
                cnt[x] = 0
                
    print(res)

if __name__ == '__main__':
    main()