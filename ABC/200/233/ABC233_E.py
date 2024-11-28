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
    X = list(map(int, input()))
    cumsum = list(accumulate(X))

    c = 0
    res = deque()
    for x in cumsum[::-1]:
        c += x
        res.appendleft(c%10)
        c //= 10
    while c:
        res.appendleft(c%10)
        c //= 10
    
    print(*res, sep='')

if __name__ == '__main__':
    main()