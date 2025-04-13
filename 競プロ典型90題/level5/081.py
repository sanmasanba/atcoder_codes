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
    MAP = [[0 for _ in range(5010)] for _ in range(5010)]
    R, C = K, K
    for _ in range(N):
        Ai, Bi = map(int, input().split())
        MAP[Ai+1][Bi+1] += 1
        R = max(R, Ai)
        C = max(C, Bi)
    R, C = R+1, C+1

    for i in range(1, R+1):
        for j in range(1, C+1):
            MAP[i][j] += MAP[i-1][j]
    for i in range(1, R+1):
        for j in range(1, C+1):
            MAP[i][j] += MAP[i][j-1]
    
    res = 0
    for i in range(R-K):
        for j in range(C-K):
            tmp = (MAP[i+K+1][j+K+1] 
                   + MAP[i][j] 
                   - MAP[i][j+K+1] 
                   - MAP[i+K+1][j])
            res = max(res, tmp)

    print(res)

if __name__ == '__main__':
    main()