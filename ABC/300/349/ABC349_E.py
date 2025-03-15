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
    N = int(input())
    C = [list(input().strip()) for _ in range(N)]    

    strs = [['' for _ in range(N)] for _ in range(N)]
    res = [[INF]*N for _ in range(N)]
    for i in range(N): 
        for j in range(N):
            if C[i][j] != '-':
                res[i][j] = 1
                strs[i][j] = C[i][j] 
            if i == j:
                res[i][j] = 0

    def f(s):
        for i in range(len(s)//2):
            if s[i] != s[i-1]:
                return False
        return True

    for k in range(N):
        for i in range(N):
            for j in range(N):
                tmp = strs[i][k] + strs[k][j]
                if f(tmp) and len(tmp) < res[i][j]:
                    strs[i][j] = tmp
                    res[i][j] = len(tmp)
        print(*res, sep='\n')
    print(*strs, sep='\n')

if __name__ == '__main__':
    main()