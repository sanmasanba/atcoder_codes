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
    N, M = map(int, input().split())
    b, X, Y, Z = [0]*N, [], [], []
    for _ in range(M):
        x, y, z = map(int, input().split())
        b[x-1] += 1
        b[y-1] += 1
        X.append(x)
        Y.append(y)
        Z.append(z)
    
    A = [0]*N
    for i, a in enumerate(b):
        if a%2==0:
            A[i] = 0

    for x, y, z in zip(X, Y, Z):
        

if __name__ == '__main__':
    main()