#library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998244353 = 998244353
MOD1000000007 = 1000000007

#prime_test
def prime_test(N):
    res = True
    for p in range(2, N):
        if p * p > N:
            break
        if N % p != 0:
            continue
        if N % p == 0:
            res = False
            break
    return res

#main
def main():
    # intput
    Q = int(input())

    pp = [i * i for i in range(2, 10**3 + 10) if prime_test(i)]
    res = []
    for _ in range(Q):
        query = int(input())
        ans = 0
        for i in range(len(pp)-1):
            square_p = pp[i]
            if query < square_p:
                break
            for j in range(i+1, len(pp)):
                square_q = pp[j]
                if query < square_p * square_q:
                    break
                p_2a = 1
                while True:
                    p_2a *= square_p
                    if query < p_2a:
                        break
                    lo = 1
                    hi = 0
                    tmp = 1
                    while True:
                        tmp *= square_q
                        hi += 1
                        if tmp > query:
                            break
                    while hi - lo > 1:
                        b = (lo + hi) // 2
                        q_2b = pow(square_q, b)
                        if p_2a * q_2b > query:
                            hi = b
                        else:
                            lo = b
                    q_2b = pow(square_q, lo)
                    if p_2a * q_2b <= query:
                        ans = max(ans, p_2a * pow(square_q, lo))
        res.append(ans)
    print(*res, sep='\n')


if __name__ == '__main__':
    main()