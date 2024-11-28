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
    S = list(input())
    S_cnt = Counter(S)

    # 1
    if len(S)%2:
        print('No')
        return
    
    # 3
    for _, cnt in S_cnt.items():
        if cnt != 2:
            print('No')
            return

    # 2
    for i in range(len(S)//2):
        if S[2*i] != S[2*i+1]:
            print('No')
            return
    
    print('Yes')

if __name__ == '__main__':
    main()