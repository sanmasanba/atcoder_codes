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
    n = int(input())
    v = list(map(int, input().split(' ')))
    
    odd_v = defaultdict(int)
    even_v = defaultdict(int)
    for i, c in enumerate(v):
        if i%2:
            odd_v[c] += 1
        else:
            even_v[c] += 1
    
    sorted_odd_v = []
    sorted_even_v = []
    for c, cnt in odd_v.items():
        sorted_odd_v.append((cnt, c))
    for c, cnt in even_v.items():
        sorted_even_v.append((cnt, c))
    sorted_odd_v.sort()
    sorted_even_v.sort()

    if len(sorted_odd_v) == 1 and len(sorted_even_v) == 1:
        if sorted_odd_v[0][1] == sorted_even_v[0][1]:
            print(sorted_odd_v[0][0])
        else:
            print(0)
    elif len(sorted_odd_v) == 1:
        print(n//2-sorted_even_v[-1][0])
    elif len(sorted_even_v) == 1:
        print(n//2-sorted_odd_v[-1][0])
    else:
        if sorted_odd_v[-1][1] == sorted_even_v[-1][1]:
            plan_a = n-sorted_odd_v[-1][0]-sorted_even_v[-2][0]
            plan_b = n-sorted_odd_v[-2][0]-sorted_even_v[-1][0]
            print(min(plan_a, plan_b))
        else:
            print(n-sorted_even_v[-1][0]-sorted_odd_v[-1][0])

if __name__ == '__main__':
    main()