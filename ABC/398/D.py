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
    N, R, C = map(int, input().split())
    S = input().strip()

    smoke = set()
    smoke.add((0, 0))
    cr, cc = 0, 0
    for c in S:        
        if c == 'N':
            R += 1
            cr += 1
        elif c == 'W':
            C += 1
            cc += 1
        elif c == 'S':
            R -= 1
            cr -= 1
        elif c == 'E':
            C -= 1
            cc -= 1
        smoke.add((cr, cc))
        
        # print(smoke, R, C)
        if (R, C) in smoke:
            print('1', end='')
        else:
            print('0', end='')

if __name__ == '__main__':
    main()