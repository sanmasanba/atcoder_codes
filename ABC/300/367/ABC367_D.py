#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, List, Tuple, Dict, TypeVar, Optional
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    # input
    N, M = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    
    cumsum = [0]
    for i in range(2*N-1):
        i %= N
        cumsum.append((cumsum[-1]+A[i])%M)

    steps = [0] * M
    for i in range(N):
        steps[cumsum[i]] += 1
    
    res = 0
    for i in range(N, 2*N):
        steps[cumsum[i-N]] -= 1
        res += steps[cumsum[i]]
        steps[cumsum[i]] += 1
    
    # output
    print(res)

if __name__ == '__main__':
    main()