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
    N, M, K = map(int, input().split())
    A, R = [], []
    for _ in range(M):
        tmp = [0]*N
        _, *AR = input().split()
        a, r = AR[:-1], AR[-1]
        for n in a: tmp[int(n)-1] = 1
        A.append(tmp)
        R.append(r == 'o')
    
    # bit_search
    res = 0
    def solve(bit):
        for a, r in zip(A, R):
            tmp = sum([a[i] * ((bit >> i)&1) for i in range(N)])
            if (K <= tmp) ^ r:
                return 0
        return 1
                    
    for bit in range(2**N):
        res += solve(bit)
    print(res)

if __name__ == '__main__':
    main()