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

# 考察の流れ
# q1 := O(1), q2 := O(N) なのでq2を減らしたい
#
# p = [3, 1, 2] に q2 が来たことを考える
# q2; p' = [2, 3, 1]
# q2; (p')' = [3, 1, 2]
# -> (p')' = p が成立するので、状態を行ったり来た入りだけでいい
#
# 置換後の配列で q1 を行う方法を考える
# 置換後の配列を r とする
# q1: swap(p[x], [py]) は、置換後も同じ関係なので swap(r[px], r[py]) 

# main
def main():
    # intput
    N, Q = map(int, input().split())
    P = list(map(lambda x: int(x)-1, input().split()))

    # 1) 配列Pと置換後の行列Qを保持してみる
    PQ = [[0]*N for _ in range(2)]
    PQ[0] = P
    for i in range(N):
        PQ[1][P[i]] = i

    # 2) query を処理
    flg = 0
    while Q:
        query = list(map(lambda x: int(x)-1, input().split()))
        if query[0] == 0:
            x, y = query[1:]
            PQ[~flg][PQ[flg][x]], PQ[~flg][PQ[flg][y]] = PQ[~flg][PQ[flg][y]], PQ[~flg][PQ[flg][x]]
            PQ[flg][x], PQ[flg][y] = PQ[flg][y], PQ[flg][x]
        else:
            flg ^= 1
        Q -= 1

    print(*[i+1 for i in PQ[flg]], sep=' ')

if __name__ == '__main__':
    main()
