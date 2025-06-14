#library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

#main
def main():
    # intput
    N, Q = map(int, input().split())
    X = list(map(int, input().split()))
    
    box = [0] * N
    res = []
    for x in X:
        if 0 < x: 
            box[x-1] += 1
            res.append(x)
        else:
            mi = 1000
            idx = 0
            for i, b in enumerate(box):
                    if b < mi: 
                        idx = i
                        mi = b
            box[idx] += 1
            res.append(idx+1)
    print(*res)

if __name__ == '__main__':
    main()