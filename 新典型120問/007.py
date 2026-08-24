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

# キーワード
# 二つの集合を比較するときは、新しい要素に共通 ID を振って
# 正規化する

# main
def main():
    # intput
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 1) 前処理をする
    # 1-1) AとBのiまでの種類数を事前計算
    a_sets, a_set = [], dict()
    for a, b in zip(A, B):
        a_set[a] = a_set.get(a, len(a_set)+1)
        a_sets.append(len(a_set))
    # 1-2) bi について登場済みなら共通ID、そうでないなら適当に
    b_sets, b_set, b_max = [], set(), []
    ma = -1
    for b in B:
        b_set.add(b)
        b_sets.append(len(b_set))

        b_id = a_set.get(b, N+10)
        ma = max(ma, b_id)
        b_max.append(ma)
    
    Q = int(input())
    for _ in range(Q):
        x, y = map(lambda x: int(x)-1, input().split())
        # 2) そこまでに登場した要素数が等しい
        # かつ、bに登場した要素の最大IDが等しいなら等しくなる
        if a_sets[x] == b_sets[y] and a_sets[x] == b_max[y]:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()
