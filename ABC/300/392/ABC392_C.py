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
    P = list(map(int, input().split()))
    q2i = {}
    i2q = {}
    for i, q in enumerate(map(int, input().split())):
        q2i[q] = i
        i2q[i] = q

    for q in range(N):
        i = q2i[q+1]
        p = P[i]
        print(i2q[p-1], end=' ')

if __name__ == '__main__':
    main()