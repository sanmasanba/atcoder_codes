#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, List, Tuple, Dict, TypeVar, Optional
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, M = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    C = list(map(int, input().split(' ')))
    
    B = [0] * (M+1)
    a_min = 0
    for nm in range(N+M, N-1, -1):
        c = C[nm]
        for n in range(max(0, N-a_min), N):
            m = nm - n
            c -= A[n]*B[m]
        B[nm-N] = c//A[-1]
        a_min += 1
    print(*B)

if __name__ == '__main__':
    main()