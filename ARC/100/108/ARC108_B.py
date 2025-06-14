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
    S = list(input().strip())
    
    res = 0
    stack = []
    for s in S:
        if s == 'x':
            if 2 <= len(stack) and stack[-2] == 'f' and stack[-1] == 'o':
                stack.pop()
                stack.pop()
            else:
                stack.append(s)
        else:
            stack.append(s)
    
    print(len(stack))

if __name__ == '__main__':
    main()