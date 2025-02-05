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
    
    if N < 3:
        print('Yes')
        return

    for i in range(N-2):
        ai_1 = A[i]
        ai_2 = A[i+1]
        ai_3 = A[i+2]
        if ai_2**2 != ai_1*ai_3:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()