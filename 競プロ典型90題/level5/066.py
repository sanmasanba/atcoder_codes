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
    L, R = map(list, zip(*[list(map(int, input().split(' '))) for _ in range(N)]))

    res = 0
    for idx in combinations(range(N), 2):
        id1, id2 = idx
        if id1 > id2:
            id1, id2 = id2, id1
        l1, r1 = L[id1], R[id1]
        l2, r2 = L[id2], R[id2]
        over = 0
        chil = 0
        for i in range(l1, r1+1):
            for j in range(l2, r2+1):
                over += 1
                if i > j:
                    chil += 1
        res += (chil*10**7)/over

    print(res/(10**7))

if __name__ == '__main__':
    main()