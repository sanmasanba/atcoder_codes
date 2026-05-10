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
    S = list(input().strip())
    
    A = [0]*(len(S)+1)
    C = [0]*(len(S)+1)
    Q = [0]*(len(S)+1)
    for i, c in enumerate(S):
        A[i+1] = A[i] + (1 if c == 'A' else 0)
        C[i+1] = C[i] + (1 if c == 'C' else 0)
        Q[i+1] = Q[i] + (1 if c == '?' else 0)
    
    res = 0
    print(A)
    print(C)
    print(Q)
    for i in range(1, len(S)):
        if S[i] == 'B' or S[i] == '?':
            l_q = Q[i]
            r_q = Q[-1] - Q[i+1]
            print((3**l_q)*max(1, A[i]) * (3**r_q)*max(1, (C[-1] - C[i+1])), 
                  A[i] * r_q, 
                  l_q * (C[-1] - C[i+1]), 
                  l_q * r_q)
            # A + (B or ?) + C
            res = (res + (3**l_q)*max(1, A[i]) * (3**r_q)*max(1, (C[-1] - C[i+1]))) % MOD1e7
            # A + (B or ?) + ?
            res = (res + A[i] * r_q) % MOD1e7
            # ? + (B or ?) + C
            res = (res + l_q * (C[-1] - C[i+1])) % MOD1e7
            # ? + (B or ?) + ?
            res = (res + l_q * r_q) % MOD1e7
        res %= MOD1e7

    print(res%MOD1e7)

if __name__ == '__main__':
    main()