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
    
    for i in range(N):
        if N < i**2:
            break
        k = i

    res = 0
    i = 1
    while i <= k:
        res += i * (N//i - N//(i+1))
        i += 1
    i = 1
    while i <= N//(k+1):
        res += N//i
        i += 1

    print(res)

if __name__ == '__main__':
    main()