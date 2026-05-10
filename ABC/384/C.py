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
    points = list(map(int, input().split(' ')))
    res = []

    chrs = "ABCDE"
    for bit in range(1, 2**5):
        total = 0
        name = ""
        for i in range(5):
            if (bit >> i) & 1:
                total += points[i]
                name += chrs[i]
        res.append((total, name))

    res.sort(key=lambda x: (-x[0], x[1])) 
    for r in res:
        print(r[1])       

if __name__ == '__main__':
    main()