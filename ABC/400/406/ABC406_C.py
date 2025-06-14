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
    P = list(map(int, input().split()))
    
    memo_A = [0]*(N)
    memo_V = [0]*(N)
    for i in range(N):
        if 0 < i <= N-2:
            memo_A[i] = memo_A[i-1] + (1 if P[i-1] < P[i] > P[i+1] else 0)
            memo_V[i] = memo_V[i-1] + (1 if P[i-1] > P[i] < P[i+1] else 0)
        else:
            memo_A[i] = memo_A[i-1]
            memo_V[i] = memo_V[i-1]

    res = 0
    for l in range(N-3):
        if P[l] > P[l+1]: continue
        A, V = memo_A[l], memo_V[l]
        a_pos, v_pos = bisect_left(memo_A, A+1), bisect_left(memo_V, V+1)
        if N <= a_pos or N <= v_pos: continue
        a_pos_ = bisect_left(memo_A, A+2)
        if a_pos_ == N: a_pos_ -= 1
        res += a_pos_ - v_pos
    
    print(res)

if __name__ == '__main__':
    main()