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
    S = list(input().strip())
    T = list(input().strip())
    N, M = len(S), len(T)

    # 各文字の出現位置を記録
    idx = [[] for _ in range(26)]
    for i, c in enumerate(S):
        idx[ord(c)-97].append(i)
    for v in idx:
        v.append(N)

    res = 0
    # i は部分列開始位置
    for i in range(N):
        # 最初の文字を入れいたのでbias
        rig = i - 1
        for j in range(M):
            c = ord(T[j]) - 97
            k = bisect_right(idx[c], rig)
            # j文字目の出現位置で更新
            rig = idx[c][k]
            if rig == N:
                break
        # 部分列は[i, rig)で構成される
        res += rig - i
    print(res)

if __name__ == '__main__':
    main()