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
    N = int(input())
    primes = eratosthenes(3000000)

    res = set()
    for p in primes:
        P = p**2
        for q in primes:
            if p == q:
                continue
            t = P*(q**2)
            if N < t:
                break
            res.add(t)
    for p in primes:
        P = p**8
        if N < P:
            break
        res.add(P)

    print(len(res))

if __name__ == '__main__':
    main()