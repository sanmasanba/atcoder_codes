#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop, heapify
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
    N, M = map(int, input().split())
    A = list(map(lambda x: -int(x), input().split()))
    # heap
    heapify(A)
    BC = []
    for _ in range(M):
        B, C = map(int, input().split())
        heappush(BC, (-C, B))

    res = []
    while len(res) < N:
        if A and BC:
            # 最大値を取り出す
            a = -heappop(A)
            c, b = heappop(BC)
            c *= -1
            if a > c:
                res.append(a)
                heappush(BC, (-c, b))
            else:
                res.extend([c]*b)
                heappush(A, -a)
        elif A:
            a = -heappop(A)
            res.append(a)
        elif BC:
            bc, b = heappop(BC)
            c *= -1
            res.extend([c]*b)

    print(sum(res[:N]))

if __name__ == '__main__':
    main()