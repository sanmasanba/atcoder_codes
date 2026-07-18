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
    M = int(input())
    N = 3
    S1 = input().strip()
    S2 = input().strip()
    S3 = input().strip()
    res = INF
    for i in range(N*M):
        for j in range(N*M):
            for k in range(N*M):
                if (i != j 
                    and j != k 
                    and k != i
                    and S1[i%M] == S2[j%M] == S3[k%M]):
                    res = min(res, max(i, j, k))
    print(res if res < INF else -1)

if __name__ == '__main__':
    main()