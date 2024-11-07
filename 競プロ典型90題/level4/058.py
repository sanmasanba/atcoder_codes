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
    N, K = map(int, input().split(' '))
    
    seen = [-1 for i in range(100000)]

    z = N
    while K > 0:
        x = z
        if seen[x] != -1:
            break
        y = sum(map(int, list(str(x))))
        z = (x + y) % 100000
        seen[x] = z
        K -= 1
    if K == 0:
        print(z)
        return 

    loop_dist = 0
    s = x
    while seen[x] != s:
        x = seen[x]
        loop_dist += 1
    K %= loop_dist+1
    x = s
    while K > 0:
        x = seen[x]
        K -= 1
    print(x)

if __name__ == '__main__':
    main()