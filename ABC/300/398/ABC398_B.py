#library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998244353 = 998244353
MOD1000000007 = 1000000007

#main
def main():
    # intput
    A = list(map(int, input().split()))
    cnt = Counter(A)

    
    vs = [v for _, v in cnt.items()]
    if len(vs) < 2:
        print('No')
        return
    for (a, b) in combinations(vs, 2):
        if (2 <= a and 3 <= b) or (3 <= a and 2 <= b):
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()