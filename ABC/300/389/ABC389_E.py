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
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    price_num = []
    for i, p in enumerate(P):
        heappush(price_num, (p, i))

    memo = [0]*N
    cost = 0
    res = 0
    while cost < M:
        p, item_num = heappop(price_num)
        if M < (cost + P[item_num]*(2*memo[item_num] + 1)):
            break
        
        cost += P[item_num]*(2*memo[item_num] + 1)
        res += 1

        memo[item_num] += 1
        p = P[item_num]*(2*memo[item_num] + 1)
        heappush(price_num, (p, item_num))

    print(res)

if __name__ == '__main__':
    main()