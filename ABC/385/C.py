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
    H = list(map(int, input().split()))
    
    res = 1
    for step in range(1, N):
        for start in range(N):
            cnt = 0
            for i in range(start, N, step):
                if H[start] != H[i]:
                    break
                cnt += 1
            res = max(res, cnt)
    print(res)

if __name__ == '__main__':
    main()