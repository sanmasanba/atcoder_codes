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
from copy import deepcopy

T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    # intput
    N, M, L = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    B = [(b, i) for i, b in enumerate(B)]
    B.sort(reverse=True)
    CL = [set() for _ in range(N)]
    for _ in range(L):
        c, l = map(lambda x: int(x)-1, input().split(' '))
        CL[c].add(l)

    res = 0
    for a in range(N):
        for b, i in B:
            if i in CL[a]:
                continue
            res = max(res, A[a]+b)
            break
    
    print(res)

if __name__ == '__main__':
    main()