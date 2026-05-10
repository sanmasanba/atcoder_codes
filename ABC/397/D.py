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

def solver(a, b, c):
    # a*x^2 + b*x + c = 0
    l, r = 0, 600000001
    while r-l > 1:
        mid = (l+r)//2
        if a*mid*mid + b*mid + c <= 0:
            l = mid
        else:
            r = mid
    if a*l*l + b*l + c == 0:
        return l
    return -1

#main
def main():
    # intput
    N = int(input())
    
    d = 0
    while d**3 <= N:
        # x^3 - y^3 = (x - y)*(x^2 + x*y + y^2)
        #           = d*(x ^ 2 + x*y + y^2)    (x - y = dとする)
        # d^2 = x^2 - 2*x*y + y^2 <= x^2 + x*y + y*2 より
        # d^3 <= d*(x^2 + x*y + y^2) = N を満たす
        # よって、(k+d)^3 - k^3 = N となる整数kをかんがえればよい

        # (k+d)^3 - k^3 = d^3 + 3*d^2*k + 3*d*k^2 = N
        d += 1
        if N%d:
            continue
        # N//d = 3*k^2 + 3*d*k + d^2
        m = N//d
        k = solver(3, 3*d, d*d-m)
        if 0 < k:
            print(k+d, k)
            return
    print(-1)
    return

if __name__ == '__main__':
    main()