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
    res = 0
    for p in range(2, N):
        if p * p > N:
            break
        if N % p != 0:
            continue
        e = 0
        while N % p == 0:
            e += 1
            N //= p
        res += e
    if N != 1:
        res += 1
    return res

#main
def main():
    # intput
    N = int(input())
    A = list(map(int, input().split(' ')))
    
    A_grundy = [prime_factorization(a) for a in A]

    XOR_SUM = 0
    for xi in A_grundy:
        XOR_SUM ^= xi
    
    print('Anna' if XOR_SUM != 0 else 'Bruno')

if __name__ == '__main__':
    main()