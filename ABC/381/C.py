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
    S = input()
    
    rle = []
    t = None
    cnt = 0
    for s in S:
        if t is None:
            t = s
            cnt += 1
            continue
        if t != s:
            rle.append((t, cnt))
            t = s
            cnt = 1
        else:
            cnt += 1
    rle.append((t, cnt))
    
    res = 0
    for s in S:
        if s == '/':
            res = 1
            break

    for i in range(1, len(rle)-1):
        if rle[i-1][0] != '1' or rle[i][0] != '/' or rle[i+1][0] != '2':
            continue
        if rle[i][1] != 1:
            continue
        res = max(res, 1 + 2*min(rle[i-1][1], rle[i+1][1])) 
    print(res)

if __name__ == '__main__':
    main()