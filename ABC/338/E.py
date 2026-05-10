#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    # intput
    N = int(input())
    circle = [() for _ in range(2*N)]
    for i in range(N):
        a, b = map(lambda x: int(x)-1, input().split())
        a, b = min(a, b), max(a, b)
        circle[a] = (0, i)
        circle[b] = (1, i)
    
    stack = []
    for i in range(2*N):
        t, idx = circle[i]
        if not t:
            stack.append(idx)
        else:
            if stack[-1] != idx:
                print('Yes')
                return
            stack.pop()
    print('No')

if __name__ == '__main__':
    main()