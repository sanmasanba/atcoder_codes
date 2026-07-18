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
    N = int(input())
    H = list(map(int, input().split()))
    
    res = 0
    for k in range(1, max(2, N)):
        for i in range(N):
            tmp = 0
            for j in range(i, N, k):
                if H[i] != H[j]:
                    break
                tmp += 1
            res = max(res, tmp)
    print(res)

if __name__ == '__main__':
    main()