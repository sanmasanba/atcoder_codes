#library
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

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

#main
def main():
    # intput
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))

    # 部分列Bの要素biはY <= bi <= Xを満たすため
    # not (Y <= ai <= X)なaiで分割すればよい
    candidate = []
    tmp = []
    min_a, max_a = INF, -INF
    for a in A:
        if not (Y <= a <= X):
            if tmp and min_a == Y and max_a == X:
                candidate.append(tmp)
            tmp = []
            min_a, max_a = INF, -INF
        else:
            min_a, max_a = min(min_a, a), max(max_a, a)
            tmp.append(a)
    if tmp and min_a == Y and max_a == X:
        candidate.append(tmp)

    res = 0
    # 部分列Bについて考える
    for S in candidate:
        cumsum_y, cumsum_x = [0], [0]
        # X、Yについて出現数の累積和を取る
        for s in S:
            # max
            cumsum_x.append(cumsum_x[-1] + (1 if s == X else 0))
            # min
            cumsum_y.append(cumsum_y[-1] + (1 if s == Y else 0))
        # Bについて、左端をl(<len(B))で固定する
        # 初めて、Y(あるいはＸ)が出る位置をminl(maxl)とすると
        # lを左端とするBの最短部分列Cが条件を満たすのはr = max(minl, maxl)
        # したがって、minlとmaxlについてそれぞれ二分探索を行えば各Bについて
        # O(log(B))で計算可能
        for l in range(len(S)):
            min_l, min_r = l, len(cumsum_y)
            if S[l] != Y:
                while min_l+1 < min_r:
                    mid = (min_l + min_r)//2
                    if 0 < (cumsum_y[mid]-cumsum_y[l]):
                        min_r = mid
                    else:
                        min_l = mid
            max_l, max_r = l, len(cumsum_x)
            if S[l] != X:
                while max_l+1 < max_r:
                    mid = (max_l + max_r)//2
                    if 0 < (cumsum_x[mid]-cumsum_x[l]):
                        max_r = mid
                    else:
                        max_l = mid
            pos = max(min_l, max_l)
            if min_l == len(S) or max_l == len(S):
                continue
            res += len(S) - pos

    print(res)

if __name__ == '__main__':
    main()