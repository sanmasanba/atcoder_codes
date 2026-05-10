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
    N = list(input())
    l1, l2, l3 = 0, 0, 0
    for n in N:
        if n == '1': l1 += 1
        if n == '2': l2 += 1
        if n == '3': l3 += 1

    if l1 == 1 and l2 == 2 and l3 == 3:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()