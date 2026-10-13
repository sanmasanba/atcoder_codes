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

# main
def main():
    # intput
    N, M, K = map(int, input().split())
    X, Y = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    # B 側をそれぞれ買うのに必要なKドル札と増える1ドルを前計算
    cB = [0] * M
    nA = [0] * M
    y = Y
    for i, b in enumerate(B):
        tmp = (b + K - 1) // K
        if y < tmp:
            break
        cB[i] = tmp
        nA[i] = K*tmp - b
        y -= tmp

    # B側を何個まで買うかを固定してみる
    cA = list(accumulate(A))

    # Aだけ買うパターンを暫定解とする
    res = 0
    for i in range(N):
        if cA[i] > X + K*Y:
            break
        res = i + 1
    
    used_k = 0
    new_1d = 0
    for b_cnt, (k, x) in enumerate(zip(cB, nA), start=1):
        # k == 0 のとき、そもそもここまで購入できないのでパターンにない
        if k == 0:
            break
        # b_cnt 個までは買えたとする
        used_k += k
        new_1d += x
        # (B の自販機からでた 1d) + X + 未使用のKドル札
        total_1d = new_1d + X + (Y - used_k) * K

        # 残りで購入できるだけ、Aのものを安いほうから買う
        idx = bisect_right(cA, total_1d)
        res = max(res, b_cnt+idx)

    print(res)

if __name__ == '__main__':
    main()
