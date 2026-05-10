#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    # intput
    N = int(input())
    A = list(map(int, input().split()))
    
    pluses = 0
    minuses = 0
    zeros = 0
    for i in range(N):
        if 0 < A[i]:   pluses += 1
        elif A[i] < 0: minuses += 1
        else:          zeros += 1
    
    res = 0
    if minuses%2 == 0: 
        for i in range(N): res += abs(A[i])
    elif 0 < zeros:
        for i in range(N): res += abs(A[i])
    else:
        mi = INF
        for i in range(N): 
            mi = min(mi, abs(A[i]))
            res += abs(A[i])
        res -= 2*mi
    
    print(res)

if __name__ == '__main__':
    main()