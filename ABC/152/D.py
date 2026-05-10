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
    MAP = [[0]*10 for _ in range(10)]

    for n in range(N+1):
        top, bottom = str(n)[0], str(n)[-1]
        MAP[int(top)][int(bottom)] += 1
    
    res = 0
    for i in range(1, 10):
        for j in range(1, 10):
            res += MAP[i][j] * MAP[j][i]
    print(res)

if __name__ == '__main__':
    main()