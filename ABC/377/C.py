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
def is_out_of_range(x:int, y:int, Xmi:int, Xma:int, Ymi:int, Yma:int) -> bool:
    if Xmi <= x < Xma and Ymi <= y < Yma:
        return False
    else:
        return True

#main
def main():
    # intput
    N, M = map(int, input().split(' '))
    can_get_set = set()
    A, B = [], []
    for _ in range(M):
        a, b = map(int, input().split(' '))
        A.append(a)
        B.append(b)
        can_get_set.add((a, b))

    res = pow(N, 2)
    move = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    for m in range(M):
        a, b = A[m], B[m]
        for dx, dy in move:
            x = a + dx
            y = b + dy
            if is_out_of_range(x, y, 1, N+1, 1, N+1):
                continue
            can_get_set.add((x, y))
    
    print(res - len(can_get_set))

if __name__ == '__main__':
    main()