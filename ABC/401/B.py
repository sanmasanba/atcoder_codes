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
    N = int(input())
    cnt = 0
    status = 0
    for _ in range(N):
        s = input().strip() 
        if s == 'login':
            status = 1
        elif s == 'logout':
            status = 0
        elif s == 'public':
            pass
        elif s == 'private':
            if status == 1:
                pass
            elif status == 0:
                cnt += 1
    print(cnt)

    

if __name__ == '__main__':
    main()