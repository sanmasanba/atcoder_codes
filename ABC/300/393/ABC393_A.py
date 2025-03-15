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
    S = list(input().split())
    
    i = ('1' if S[0] == 'sick' else '0') + ('1' if S[1] == 'sick' else '0')
    if i == '11':
        print(1)
    elif i == '10':
        print(2)
    elif i == '01':
        print(3)
    elif i == '00':
        print(4)

if __name__ == '__main__':
    main()