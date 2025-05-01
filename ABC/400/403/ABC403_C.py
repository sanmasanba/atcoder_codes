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
MOD998 = 998244353
MOD1e7 = 1000000007

#main
def main():
    # intput
    N, M, Q = map(int, input().split())
    
    ALL = set(i for i in range(M))
    users_permission = {i:set() for i in range(N)}
    for _ in range(Q):
        input_ = input().strip()
        if input_[0] == '1':
            _, x, y = map(lambda x: int(x)-1, input_.split())
            users_permission[x].add(y)
        elif input_[0] == '2':
            _, x = map(lambda x: int(x)-1, input_.split())
            users_permission[x] = ALL
        elif input_[0] == '3':
            _, x, y = map(lambda x: int(x)-1, input_.split())
            if y in users_permission[x]:
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    main()