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
MOD998244353 = 998244353
MOD1000000007 = 1000000007

#main
def main():
    # intput
    N, K = map(int, input().split())
    MAP = [[0 for _ in range(5001)] for _ in range(5001)]
    for _ in range(N):
        Ai, Bi = map(int, input().split())
        MAP[Ai][Bi] += 1
    
    for i in range(5000):
        tmp = 0
        for j in range(5000):
            MAP[i][j] += tmp
            tmp = MAP[i][j]  
    for j in range(5000):
        tmp = 0
        for i in range(5000):
            MAP[i][j] += tmp
            tmp = MAP[i][j]


if __name__ == '__main__':
    main()