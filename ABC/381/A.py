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
    S = input()
    l = S.split('/')

    if len(l) == 2 and len(l[0]) == len(l[1]) and all([s == '1' for s in l[0]]) and all([s == '2' for s in l[1]]):
        print('Yes')
    else:
        print('No')    

if __name__ == '__main__':
    main()