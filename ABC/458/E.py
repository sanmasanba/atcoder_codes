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

fact, fact_inv, inv = [], [], []
def init_nCk(n):
    """
    nCkを計算に用いる逆元と階乗の事前計算

    Args:
        n (int): nの上限
    """
    global fact, fact_inv, inv
    fact = [0] * (n+10)
    fact_inv = [0] * (n+10)
    inv = [0] * (n+10)
    fact[0], fact[1] = 1, 1
    fact_inv[0], fact_inv[1] = 1, 1
    inv[1] = 1
    for i in range(2, n+10):
        fact[i] = fact[i-1] * i % MOD998
        inv[i] = MOD998 - inv[MOD998%i] * (MOD998//i) % MOD998
        fact_inv[i] = fact_inv[i-1] * inv[i] % MOD998

def nCk(n, k):
    """
    nCk mod PをO(1)で返す

    Args:
        n (int): 全ての数
        k (int): 選ぶ数

    Returns:
        int: 計算結果
    """
    global fact, fact_inv, inv
    assert not (n < k)
    assert not ((n < 0) or (k < 0))
    return fact[n] * (fact_inv[k] * fact_inv[n-k] % MOD998) % MOD998

# main
def main():
    # intput
    X1, X2, X3 = map(int, input().split())
    N = X1 + X2 + X3

    init_nCk(N)
    res = 0
    # `2`によって分割された X2+1 個の区間のうち k 個に`1`が入る
    for k in range(1, X2+1):
        # r1: X2+1 個の区間から、k 個を選ぶ組み合わせ
        r1 = nCk(X2+1, k) if X2+1 >= k else 0
        # r2: X1 個の`1`のうち、 k 個に分割する組み合わせ
        r2 = nCk(X1-1, k-1) if X1 >= k else 0
        # r1 で選択された区間には、`3`をいれることはできない
        # `1` -> `3` あるいは `3` -> `1` が発生するので、規約違反
        # r3: X3 を残りの区間に詰め込むことのできる組み合わせ
        # =>    (X2-k+1)にX3を 0 個以上ずつ詰め込むのは、X3+(`区間の数`-1)から
        #       どれを区間の仕切りするかを選ぶのに等しい
        r3 = nCk(X2+X3-k, X2-k)
        res = (res + ((r1 * r2)%MOD998 * r3)%MOD998)%MOD998
    print(res)

if __name__ == '__main__':
    main()