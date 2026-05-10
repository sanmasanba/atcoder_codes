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
    N, C = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    
    if N == 1:
        print(1)
        return 
    
    pre_t = A[0]
    res = 1
    for t in A[1:]:
        if t - pre_t >= C:
            res += 1
            pre_t = t

    print(res)

if __name__ == '__main__':
    main()