# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, isqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, NamedTuple, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

# eratosthenes
def eratosthenes(N: int) -> List[int]:
    if N < 2:
        return []
    isprime = [True] * (N+1)

    isprime[0], isprime[1] = False, False

    for p in range(2, isqrt(N)+1):
        if not isprime[p]:
            continue

        q = p * p
        while q <= N:
            isprime[q] = False
            q += p

    return [i for i, e in enumerate(isprime) if e]

# main
def main():
    # intput
    S = list(input().strip())
    
    prime = set(eratosthenes(10000000))

    d = list(set(S))
    

    for perm in permutations(range(10), len(d)):
        cnv = {dd: pp for dd, pp in zip(d, perm)}
        tmp = 0
        for s in S:
            tmp *= 10
            tmp += cnv[s]
        if 10**(len(S)-1) <= tmp < 10**len(S) and tmp in prime:
            print(tmp)
            return
    print(-1)

if __name__ == '__main__':
    main()
