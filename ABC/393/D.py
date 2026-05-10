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
    S = list(input().strip())
    
    positions = []
    for i in range(N):
        if S[i] == '1':
            positions.append(i)
    if len(positions) == 1:
        print(0)
        return

    start = len(positions)//2

    res = INF
    for i in range(start, start+2):
        if len(positions) <= i:
            continue
        tmp = 0
        center = positions[i]
        for j in range(len(positions)):
            if i == j:
                continue
            tmp += abs(positions[i]-positions[j]) - abs(i-j)
        res = min(res, tmp)
    print(res)

if __name__ == '__main__':
    main()