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
    S = list(input().strip())

    if len(S) == 1:
        print(''.join(S))
        return
    
    for i in range(len(S)-1, 0, -1):
        if S[i-1] == 'W' and S[i] == 'A':
            S[i-1] = 'A'
            S[i] = 'C'
    print(''.join(S))

if __name__ == '__main__':
    main()