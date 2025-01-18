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
    N, M = map(int, input().split())
    A = [list(input()) for _ in range(N)]
    B = [list(input()) for _ in range(M)]

    def check(i, j):
        M = len(B)
        for di in range(M):
            for dj in range(M):
                if A[i+di][j+dj] != B[di][dj]:
                    return False
        return True

    for i in range(N-M+1):
        for j in range(N-M+1):
            if check(i, j):
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()