#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate, combinations_with_replacement
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    # intput
    N, M, Q = map(int, input().split(' '))
    a, b, c, d = [0]*Q, [0]*Q, [0]*Q, [0]*Q
    for i in range(Q):
        ai, bi, ci, di = map(int, input().split(' '))
        a[i] = ai-1
        b[i] = bi-1
        c[i] = ci
        d[i] = di
    
    res = 0
    for perm in combinations_with_replacement(range(1, M+1), N):
        A = list(perm)
        if all([A[i] <= A[i+1] for i in range(N-1)]):
            tmp = 0
            for i in range(Q):
                if A[b[i]]-A[a[i]] == c[i]:
                    tmp += d[i]
            res = max(res, tmp)
    
    print(res)

if __name__ == '__main__':
    main()