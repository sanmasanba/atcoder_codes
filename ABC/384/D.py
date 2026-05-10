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
    N, S = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    
    sumA = sum(A)
    S %= sumA

    A += A
    r = 0
    tmp = 0
    for l in range(2*N):
        while l <= r < 2*N and tmp < S:
            tmp += A[r]
            r += 1
        if tmp == S:
            print('Yes')
            return
        
        tmp -= A[l]
    print('No')

if __name__ == '__main__':
    main()