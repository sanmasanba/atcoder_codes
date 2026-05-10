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
    W, H = map(int, input().split())
    N = int(input())
    p, q = zip(*[list(map(int, input().split())) for _ in range(N)])
    A = int(input())
    a = [0] + list(map(int, input().split())) + [W]
    B = int(input())
    b = [0] + list(map(int, input().split())) + [H]
    
    min_strawberry = N
    max_strawberry = 1
    
    res = defaultdict(int)
    for pi, qi in zip(p, q):
        pi_idx = a[bisect_left(a, pi, 1, A+2)]
        qi_idx = b[bisect_left(b, qi, 1, B+2)]
        
        res[(pi_idx, qi_idx)] += 1
    
    for _, v in res.items():
        max_strawberry = max(max_strawberry, v)
        min_strawberry = min(min_strawberry, v)
    if len(res) != (A+1)*(B+1):
        min_strawberry = 0
    print(min_strawberry, max_strawberry)

if __name__ == '__main__':
    main()