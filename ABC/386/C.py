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
    K = int(input())
    S = input()
    T = input()

    if S == T:
        print('Yes')
        return 

    idx = 0
    while idx < len(S) and idx < len(T) and S[idx] == T[idx]:
        idx += 1

    res = False
    res |= S[idx:] == T[idx+1:]      # insert
    res |= S[idx+1:] == T[idx:]       # delete
    res |= S[idx+1:] == T[idx+1:]     # replace

    print('Yes' if res else 'No')

if __name__ == '__main__':
    main()