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
    q, r = map(list, zip(*[list(map(int, input().split(' '))) for _ in range(N)]))
    Q = int(input())
    for _ in range(Q):
        t, d = map(int, input().split(' '))
        q_, r_ = q[t-1], r[t-1]
        if d%q_ == r_:
            print(d)
            continue
        if q_*(d//q_) <= d < q_*(d//q_) + r_:
            print(q_*(d//q_) + r_)
        else:
            print(q_*(d//q_ + 1) + r_)

if __name__ == '__main__':
    main()