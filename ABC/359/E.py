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
    H = list(map(int, input().split()))
    
    most_high = 0
    wall = 0
    start = 0
    bias = 0
    res = [0]*N
    for i, h in enumerate(H, start=1):
        if most_high < h:
            bias = h*i
            res[i-1] = bias + 1
            start = i
            wall = 0
        elif wall <= h:
            if wall != 0:
                res[i-1] = bias + h*(i-start) + 1
                bias += h*(i-start)
                wall = 0
                start = i
            else:
                res[i-1] = res[i-2] + h
                wall = h
        else:
            bias += wall*(i-1-start)
            res[i-1] = res[i-2] + h
        print(h, bias, res[i-1])
        most_high = max(most_high, h)

    print(*res)

if __name__ == '__main__':
    main()