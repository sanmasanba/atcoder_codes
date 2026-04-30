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

# main
def main():
    N, A, B = map(int, input().split())
    S = list(input().strip())
    
    a_count = [0] * (N + 1)
    b_count = [0] * (N + 1)
    for i in range(N):
        a_count[i + 1] = a_count[i] + (1 if S[i] == 'a' else 0)
        b_count[i + 1] = b_count[i] + (1 if S[i] == 'b' else 0)

    res = 0
    for l in range(1, N + 1):
        low = l
        high = N + 1
        while low < high:
            mid = (low + high) // 2
            if a_count[mid] - a_count[l - 1] >= A:
                high = mid
            else:
                low = mid + 1
        start = low

        low = l
        high = N + 1
        while low < high:
            mid = (low + high) // 2
            if b_count[mid] - b_count[l - 1] < B:
                low = mid + 1
            else:
                high = mid
        end = low - 1

        if start <= end:
            res += end - start + 1

    print(res)

if __name__ == '__main__':
    main()