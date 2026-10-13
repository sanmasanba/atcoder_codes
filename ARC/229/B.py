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

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    # 特殊はのぞく
    if all(a == 0 for a in A):
        print(0)
        return
    
    # 末尾正規化
    while A[-1] > 0:
        A.append(A[-1]//2)

    res = 0
    M = len(A)
    for i in range(M-1, 0, -1):
        # 下からの伝搬をひけない　→　失敗
        if A[i-1] < 2*A[i]:
            print(-1)
            return
        # 7, 2, 1 のとき、後ろから 4, 2, 1(res = 1)が伝搬してきている場合
        # 7 を 0 にするには、もともと引いているresに加えて新たに2つ追加
        # (4 + 1, 2, 1), (1, 0, 0) (1, 0, 0)
        res += A[i-1] - min(A[i-1], 2*A[i] + res)
    print(res)

# main
def main():
    # intput
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()
