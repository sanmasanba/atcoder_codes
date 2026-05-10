#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate, count
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
        res.append((p, e))
    if N != 1:
        res.append((N, 1))
    return res

#main
def main():
    # intput
    A, B = map(int, input().split(' '))
    
    # 公約数はすべて最大公約数の倍数になるので
    # 最大公約数だけ考える
    max_divisors = gcd(A, B)
    # 最大分割するには、最大公約数のもつ素因数の数＋１(１が必ず含まれるので)
    print(len(prime_factorization(max_divisors))+1)

if __name__ == '__main__':
    main()