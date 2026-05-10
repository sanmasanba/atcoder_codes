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
    S = list(input())
    
    res = 0
    for i in range(len(S)):        
        for l in range(1, len(S)):
            j, k = i+l, i+2*l
            if not (0 <= j < len(S)) or not (0 <= k < len(S)):
                continue
            if S[i] == 'A' and S[j] == 'B' and S[k] == 'C':
                res += 1
    print(res)

if __name__ == '__main__':
    main()