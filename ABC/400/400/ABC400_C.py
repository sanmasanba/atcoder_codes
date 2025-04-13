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
MOD998244353 = 998244353
MOD1000000007 = 1000000007

from math import isqrt

#main
def main():
    # intput
    N = int(input())
    
    # x = 2**a * b**2と表されるa, bの組み合わせは1通りしかない
    # ここで、aを固定するとx <= Nとなるときのbの範囲は
    # b <= sqrt(N / 2**a)となる
    # したがって、bの個数はfloor(sqrt(N / 2**a))になる
    # これをa = 0, 1, 2, ... , floor(log2(N))まで全探索する

    res = 0
    for a in range(1, 61):
        res += ()

if __name__ == '__main__':
    main()