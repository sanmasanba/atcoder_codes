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
    T = int(input())

    for _ in range(T):
        N, D, K = map(int, input().split())
        K -= 1
        # g := 0 -> D -> 2D ... -> 0 となる周期
        g = N//gcd(N, D)
        # i周目は、i -> D+i -> 2D+i -> ... -> i　の周期になる
        print((D*K)%N + K//g)

if __name__ == '__main__':
    main()