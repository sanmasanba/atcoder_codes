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
MOD998 = 998244353
MOD1e7 = 1000000007

#main
def main():
    # intput
    N = int(input())
    A = list(map(int, input().split()))
    
    if N == 1:
        print(A[0])
        return

    dp = [0 for _ in range(200000)]  
    for i in range(200000):
        for j in range(2, 200000, 2):
            if i+j < N:
                dp[i+j] = max(dp[i+j], dp[i])

if __name__ == '__main__':
    main()