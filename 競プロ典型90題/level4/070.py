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

def solve(A):
    l = -10**9; r = 10**9
    while l + 10**2 < r:
        mid1 = (2*l+r)//3
        mid2 = (l+2*r)//3
        dist1 = sum(abs(i-mid1) for i in A)
        dist2 = sum(abs(i-mid2) for i in A)

        if dist1 > dist2:
            l = mid1
        else:
            r = mid2
    return l, r

#main
def main():
    # intput
    N = int(input())
    X, Y = [], []
    for _ in range(N):
        x, y = map(int, input().split(' '))
        X.append(x)
        Y.append(y)

    x_min, x_max = solve(X)
    y_min, y_max = solve(Y)

    x_res, y_res = INF, INF
    for x in range(x_min, x_max+1): x_res = min(x_res, sum(abs(i-x) for i in X))
    for y in range(y_min, y_max+1): y_res = min(y_res, sum(abs(i-y) for i in Y))

    print(x_res + y_res)

if __name__ == '__main__':
    main()