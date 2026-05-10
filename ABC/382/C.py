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
    N, M = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    tmp = list(map(int, input().split(' ')))
    B = [(b, i) for i, b in enumerate(tmp)]
    B.sort(reverse=True)

    res = [-1]*M
    curr = 0
    for i, a in enumerate(A):
        while curr < M:
            b, j = B[curr]
            if a <= b:
                res[j] = i+1
            else:
                break
            curr += 1
    
    print(*res, sep='\n')

if __name__ == '__main__':
    main()