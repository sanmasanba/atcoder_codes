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

# 考察
# binom(n, k) は 最大で10**10 程度なので全列挙は無理
# f = (a + b + c)^2 を開くと
# f = a^2 + b^2 + c^2 + 2*(ab + ac + bc)
# ->　単一の式では寄与を２つずつを選ぶことに分解できる
# -> 最終的な解に何回寄与するかがわかればよさそう
# a^2 タイプは、aを固定して残りなので、(n-1)C(k-1)回の寄与
# abタイプは(n-2)C(k-2)回だけ寄与する
# -> 相異なるすべての積を求められればいい
# 
# ab タイプをすべて考えるO(n^2)なので、別の方法を使う
# (a, b, c, d, e) で考える。ここで、出てくる組み合わせを前の文字でくくる
# ab + ac + ad + ae + bc + bd + be + cd + ce + de
# = a * (b + c + d + e) + b * (c + d + c) + c * (d + e) + d * e
# -> 係数を無視すれば、自身 * (自身より後ろの要素の総和) になる
# -> 総和を事前計算O(n)で計算すれば、クエリはO(1)

# main
def main():
    # intput
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 1) 1の時はそのまま求める
    if K == 1:
        res = 0
        for a in A:
            res = (res + a**2)%MOD998
        print(res)
        return

    # 事前にnckの準備をする
    init_nCk(N+10)

    res = 0
    # 2) a^2 型の寄与は(n-1)C(k-1)
    same_conf = nCk(N-1, K-1)
    for a in A:
        res = (res + (same_conf * a**2) % MOD998)%MOD998

    # 3) ab 型の寄与は(n-2)C(k-2)
    cumsum = [0] + list(accumulate(A))
    for i, a in enumerate(A[:-1]):
        # a を固定して、後ろ側の総和だけの寄与を考える
        s = cumsum[-1] - cumsum[i+1]
        res = (res + ((2 * a * s % MOD998) * nCk(N-2, K-2)) % MOD998) % MOD998
        
    print(res)

if __name__ == '__main__':
    main()
