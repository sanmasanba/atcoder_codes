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
    N, K = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    AB = [(a, b) for a, b in zip(A, B)]
    AB.sort(key=lambda x: x[0])

    res = 0
    min_s = 0
    sampling_B = []
    for a, b in AB:
        heappush(sampling_B, -b)
        min_s += b
        if len(sampling_B) < K:
            continue
        elif len(sampling_B) == K:
            res = a * min_s
        else:
            b = heappop(sampling_B)
            min_s += b
            res = min(res, min_s*a)

    print(res)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        main()