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
    A = list(map(int, input().split(' ')))
    A_cnt = Counter(A)
    
    res = 0
    # p/r = q <=> p = qr
    for q in range(1, 200001):
        r = 1
        while r*q <= 200001:
            q_cnt = A_cnt.get(q, 0)
            r_cnt = A_cnt.get(r, 0)
            qr_cnt = A_cnt.get(q*r, 0)
            res += q_cnt * r_cnt * qr_cnt
            r += 1

    print(res)

if __name__ == '__main__':
    main()