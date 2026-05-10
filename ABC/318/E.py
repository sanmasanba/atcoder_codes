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
    A = list(map(int, input().split(' ')))
    
    nums = [[] for _ in range(N+1)]
    for i, a in enumerate(A):
        nums[a].append(i)
    
    res = 0
    for n in nums:
        diffs = []
        for i in range(len(n)-1):
            diffs.append(n[i+1]-n[i]-1)
        tmp = 0
        for i in range(len(diffs)-1, -1, -1):
            tmp += diffs[i]*(len(diffs)-i)*(i+1)
        res += tmp
    
    print(res)

if __name__ == '__main__':
    main()