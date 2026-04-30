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

def mat_mult(A: List[T], B: List[T], mod: int=MOD1e7) -> List[T]:
    """行列の内積を計算

    Args:
        A (List[T]): tensor
        B (List[T]): tensor
        mod (int, optional): Defaults to MOD1e7.

    Returns:
        List[T]: dot multiple
    """
    assert len(A) == len(A[0])
    assert len(B) == len(B[0])
    N = len(A)
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j] = (res[i][j]+A[i][k]*B[k][j]%mod)%mod
    return res

def mat_pow(mat:List[T], exp:int, mod: int=MOD1e7) -> List[T]:
    """mat pow

    Args:
        mat (List[T]): matrix
        exp (int): exponetial
        mod (int, optional): MOD. Defaults to MOD1e7.

    Returns:
        List[T]: mat pow
    """
    N = len(mat)
    res = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    while exp:
        if exp%2:
            res = mat_mult(res, mat, mod)
        mat = mat_mult(mat, mat, mod)
        exp //= 2
    return res

#main
def main():
    # intput
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    # 頂点crrから頂点toへの遷移を考えると
    # dp[K+1][to] += dp[k][crr]
    # したがって、以下の漸化式が成り立つ
    
    # a[0] = [1, 1, 1, ..., 1] (要素数N)
    # a[k+1] = A * a[k]
    #        = A * (A * A[k-1])
    # -> A[k+1] = A**k * a[0]
    # よって、A**K をもとめれば高速化できる
    mat = mat_pow(A, K, MOD1e7)

    V = [1] * N
    v_res = [sum(mat[i][j] * V[j] for j in range(N)) % MOD1e7 for i in range(N)]
    print(sum(v_res)%MOD1e7)

if __name__ == '__main__':
    main()