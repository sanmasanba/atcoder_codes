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

#prime_factorization
def prime_factorization(N) -> list:
    res = []
    for p in range(2, N):
        if p * p > N:
            break
        if N % p != 0:
            continue
        e = 0
        while N % p == 0:
            e += 1
            N //= p
        res.append(p)
    if N != 1:
        res.append(N)
    return res

#main
def main():
    # intput
    N, M = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    
    res = set(range(1, M+1))
    ps = set()
    for i in range(N):
        tmp = prime_factorization(A[i])
        for t in tmp:
            ps.add(t)
    
    for p in ps:
        a = 1
        prime = p
        while prime <= M:
            res.discard(prime)
            prime += p
    
    print(len(res))
    print(*sorted(list(res)), sep='\n')

if __name__ == '__main__':
    main()