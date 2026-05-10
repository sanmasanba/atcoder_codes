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
    H, W, N = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    A.sort()

    chocos = [(H, W)]
    while A:
        a = A.pop()
        edge = 2**a
        choco = None
        d = INF
        for c in chocos:
            h, w = c
            if edge <= h and edge <= w and min(h-edge, w-edge) < d:
                choco = (h, w)
                d = min(h-edge, w-edge)
        if choco is None:
            print('No')
            return 

        def solve(edge):
            w, h = choco
            if h-edge==0 and w-edge==0:
                return []
            elif w-edge==0:
                return [(h-edge, w)]
            else:
                return [(h-edge, w), (edge, w-edge)]

        chocos.remove(choco)
        if choco[0] > choco[1]:
            choco = (choco[1], choco[0])            
        for c in solve(edge):
            chocos.append(c)

    print('Yes')

if __name__ == '__main__':
    main()