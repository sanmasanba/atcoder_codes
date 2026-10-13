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

# 解説
# 1) A1 が決まれば残りは決まる
# A1 を x とすると
# A1 = x
# A2 = S1 - x
# A3 = S2 - A2 = S2 - S1 + x
# A4 = S3 - S2 + S1 - x
# ...
# => 適切な x を選ぶ問題に帰結
# 2) 「x を選ぶ」問題から、「x をいくつにするべきか」に
# - A1(= x) = Xj にしたい -> x = Xj
# - A2(= S1 - x) = Xj にしたい -> x = S1 - Xj
# - A3(= S2 - S1 + x) = Xj にしたい -> x = S1 - S2 + Xj
# - 同様に A4 のとき、x = x = S1 - S2 + S3 - Xj
# => Xj を固定すれば、Aiとの関係で一意に x が定まる
# => Xj ごとに、x を計算して、最も出現数のおおいxの回数が解

# main
def main():
    # intput
    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    X = list(map(int, input().split()))
    
    res = defaultdict(int)
    s = 0
    for i in range(N):
        for xj in X:
            res[s + (-1 if i%2==1 else 1)*xj] += 1
        if i != N-1:
            s += (-1 if i%2==1 else 1) * S[i]
    print(max(v for v in res.values()))

if __name__ == '__main__':
    main()
