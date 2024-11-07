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
    N, K = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    
    num_set = {}
    r = 0
    res = 0
    for l in range(N):
        while r < N:
            if A[r] not in num_set:
                if len(num_set) < K:
                    num_set[A[r]] = 1
                else:
                    break
            else:
                num_set[A[r]] += 1
            r += 1
        res = max(res, r-l)
        num_set[A[l]] -= 1
        if num_set[A[l]] == 0:
            num_set.pop(A[l])

    print(res)

if __name__ == '__main__':
    main()