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
    N = int(input())
    X, Y = zip(*[list(map(int, input().split())) for _ in range(N)])

    memo = defaultdict(int)
    for i, j in combinations(range(N), 2):
        xi, yi, xj, yj = X[i], Y[i], X[j], Y[j]
        x, y = xi - xj, yi - yj
        m = gcd(abs(x), abs(y))
        if x == 0 or y == 0:
            x, y = abs(x) ,abs(y)    
        memo[(x//m, y//m)] += 1
    
    print(memo)
    res = 0
    for k, v in memo.items():
        res += (v*(v-1))//2
    print(res)
     

if __name__ == '__main__':
    main()