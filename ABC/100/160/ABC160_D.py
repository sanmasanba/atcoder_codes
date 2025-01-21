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
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1

    res = [0]*N
    for combi in combinations(range(N), 2):
        a, b = combi 
        # a -> b
        res1 = b-a
        # a -> X -> Y -> b
        res2 = abs(X-a) + 1 + abs(Y-b)
        res[min(res1, res2)] += 1

    print(*res[1:], sep='\n')        

if __name__ == '__main__':
    main()