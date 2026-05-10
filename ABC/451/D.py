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
    # preset
    # k = 10桁以下の2のべき乗集合を定義
    P = [[] for _ in range(10)]
    for k in range(1, 10):
        l = (10**(k-1)-1).bit_length()
        r = (10**k - 1).bit_length()
        P[k] = [1<<i for i in range(l, r)]
    
    # k桁のよい整数の集合
    X = [set() for _ in range(10)]
    X[0] = {0}

    A = []
    for k in range(1, 10):
        for i in range(1, k+1):
            # xをi桁分だけシフトしたものをprefixとして、x*(10**i) + p
            X[k] |= {x*(10**i) + p for x in X[k-i] for p in P[i]}
        A.extend(list(X[k]))
    A.sort()
    # intput
    N = int(input())
    print(A[N-1])

if __name__ == '__main__':
    main()