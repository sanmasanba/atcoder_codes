#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    # intput
    N, K = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))

    B = A[K:]
    # K番目以降の要素について、i+1番目まで最大の数の数列にする
    for i in range(1, len(B)):
        B[i] = max(B[i], B[i-1])

    res = INF
    for i in range(K):
        # A[i]より大きい要素の最小のインデックスを調べる
        pos = bisect_right(B, A[i])
        if pos == len(B):
            continue
        # ..., i, i+1, ..., j-1, j, ...
        # となるとき、入れ替え回数はj-i回
        res = min(res, (pos + K) - i)
    
    print(-1 if res == INF else res)

if __name__ == '__main__':
    main()