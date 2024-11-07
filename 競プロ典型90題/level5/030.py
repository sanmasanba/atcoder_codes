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

# eratosthenes
def eratosthenes(N: int) -> List[int]:
    isprime = [True] * (N+1)

    isprime[0], isprime[1] = False, False

    for p in range(2, N+1):
        if not isprime[p]:
            continue

        q = p * 2
        while q <= N:
            isprime[q] = False
            q += p

    return [i for i, e in enumerate(isprime) if e]

#main
def main():
    # intput
    N, K = map(int, input().split(' '))
    prime_list = eratosthenes(10**7+10)
    prime_set = [0 for _ in range(10**7+10)]
    for prime in prime_list:
        for i in range(prime, N+1, prime):
            prime_set[i] += 1
    
    # output
    res = [i for i, j in enumerate(prime_set) if K <= j]
    print(len(res))

if __name__ == '__main__':
    main()