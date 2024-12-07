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
    T, V = map(list, zip(*[list(map(int, input().split(' '))) for _ in range(N)]))
    
    p = 0
    res = 0
    for t, v in zip(T, V):
        tmp = t-p
        res = max(0, res-tmp)
        res += v
        p = t

    print(res)

if __name__ == '__main__':
    main()