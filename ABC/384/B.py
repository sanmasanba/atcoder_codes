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
    N, R = map(int, input().split(' '))
    D, A = [], []
    for _ in range(N):
        d, a = map(int, input().split(' '))
        D.append(d)
        A.append(a)
    
    for d, a in zip(D, A):
        if d == 1 and 1600 <= R <= 2799:
            R = max(0, R+a)
        elif d == 2 and 1200 <= R <= 2399:
            R = max(0, R+a)
    
    print(R)

if __name__ == '__main__':
    main()