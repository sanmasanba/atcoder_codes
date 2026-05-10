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
    N, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    
    res = 0
    que = deque()
    product = 1
    for a in A:
        if a == 0:
            print(N)
            return 
        
        que.append(a)
        product *= a

        while que and product > K:
            remove = que.popleft()
            product //= remove
        res = max(res, len(que))
    
    print(res)

if __name__ == '__main__':
    main()