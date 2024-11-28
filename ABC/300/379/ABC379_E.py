#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate, zip_longest
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    # intput
    N = int(input())
    S = list(input())
    
    # 各桁をi倍して、足しておく
    A = [(i+1) * int(S[i]) for i in range(N)]
    for i in range(1, N): A[i] += A[i-1]

    i = 0
    c = 0
    res = []
    while i < N or c > 0:
        # 最大桁より小さい間は、その桁の足し算をｃに足す
        if i < N:
            c += A[N-1-i]
        # 今のcの１の位が、現在の位の答えでそれ以上の値はより
        # 上位の桁の計算に繰り越す
        res.append(c%10)
        c //= 10
        i += 1
    print(*res[::-1], sep='')

if __name__ == '__main__':
    main()