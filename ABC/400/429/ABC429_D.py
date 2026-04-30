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

def comp(N, A):
    tmp = sorted(list(set(A)))
    P = [0]*len(tmp)
    n2i, i2n = {}, {}
    for i, a in enumerate(tmp):
        n2i[a] = i
        i2n[i] = a
    for i in range(N): P[n2i[A[i]]] += 1
    return P, tmp

# main
def main():
    # intput
    N, M, C = map(int, input().split())
    A = list(map(int, input().split()))
    P, Q = comp(N, A)
    Q.append(M)
    if Q[0] != 0:
        Q = [0] + Q
        P = [0] + P
    cumsum = list(accumulate(P + P))

    # binary search
    def binary_search(array, i):
        # 最大と最小の設定
        ng = i
        ok = len(array)
    
        while ok - ng > 1:
            mid = (ng + ok) // 2
            v = array[mid] - array[i]
            if C <= v:
                ok = mid
            else:
                ng = mid
        return array[ok]-array[i]

    res = 0
    for i in range(len(Q)-1):
        tmp = (Q[i+1]-Q[i])*binary_search(cumsum, i)
        res += tmp
    print(res)

if __name__ == '__main__':
    main()