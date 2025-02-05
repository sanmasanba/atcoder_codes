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
    A = list(map(int, input().split()))
    
    N = min(8, N)
    memo = [[] for _ in range(200)] 
    for bit in range(2**N):
        s = []
        SUM = 0
        for i in range(N):
            if bit >> i & 1:
                s.append(i+1)
                SUM = (SUM+A[i])%200
        if memo[SUM]:
            print('Yes')
            print(len(memo[SUM]), *memo[SUM])
            print(len(s), *s)
            return
        else:
            memo[SUM] = s
    print('No')

if __name__ == '__main__':
    main()