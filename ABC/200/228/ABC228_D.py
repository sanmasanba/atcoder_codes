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

def find(P, h):
    if P[h] == h:
        return h
    else:
        P[h] = find(P, P[h])
        return P[h]

#main
def main():
    # intput
    Q = int(input())
    N = 2**20
    A = [-1] * N
    P = [i for i in range(N)]

    for _ in range(Q):
        t, x = map(int, input().split(' '))
        match t:
            case 1:
                h = find(P, x%N)
                A[h] = x
                P[h] = find(P, (h+1)%N)
            case 2:
                print(A[x%N])
    
if __name__ == '__main__':
    main()