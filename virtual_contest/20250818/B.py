# library
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
        fact[i] = fact[i-1] * i % MOD1e7
        inv[i] = MOD1e7 - inv[MOD1e7%i] * (MOD1e7//i) % MOD1e7
        fact_inv[i] = fact_inv[i-1] * inv[i] % MOD1e7

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
    return fact[n] * (fact_inv[k] * fact_inv[n-k] % MOD1e7) % MOD1e7

# main
def main():
    # intput
    S = int(input())
    init_nCk(S)
    res = 0
    # 数列の長さk
    for k in range(1, S//3+1):
        # すべての要素から-3する → S-3k
        # → S-3k個のボールにk-1個の仕切りを入れる並べ方の数に等しい
        # (S-3k+k-1)C(k-1) → (S-2k-1)C(k-1)
        res = (res + nCk(S-2*k-1, k-1))%MOD1e7
    print(res%MOD1e7)

if __name__ == '__main__':
    main()