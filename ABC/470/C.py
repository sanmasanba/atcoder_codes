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
    N, Q = map(int, input().split())
    A = [0]*N
    # 1) ai >= 1 な要素のみ保持する
    idxs = []

    res = 0
    for _ in range(Q):
        query = list(input().split())
        if query[0] == "1":
            x = int(query[1]) - 1
            if A[x] == 0:
                idxs.append(x)
            res ^= A[x] ^ (A[x] + 1) 
            A[x] += 1
        else:
            # query 1 は最大でQ回なので、O(Q)にしかならない
            for idx in idxs:
                res ^= A[idx] ^ (A[idx] - 1)
                A[idx] -= 1
            idxs = [idx for idx in idxs if A[idx] != 0]
        print(res)

if __name__ == '__main__':
    main()