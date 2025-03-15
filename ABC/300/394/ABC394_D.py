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
    S = list(input().strip())

    stack = []
    for s in S:
        stack.append(s)
        if 1 < len(stack):
            if stack[-2] == '(' and stack[-1] == ')':
                stack.pop()
                stack.pop()
            elif stack[-2] == '[' and stack[-1] == ']':
                stack.pop()
                stack.pop()
            elif stack[-2] == '<' and stack[-1] == '>':
                stack.pop()
                stack.pop()
    
    print('Yes' if not stack else 'No')


if __name__ == '__main__':
    main()