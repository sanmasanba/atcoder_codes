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
MOD = 998244353

#main
def main():
    # intput
    N = int(input())
    D = list(map(int, input().split()))

    max_depth = max(D)
    depth2num = [0]*(max_depth+1)
    for d in D: depth2num[d] += 1

    if 1 != depth2num[0] or D[0] != 0:
        print(0)
        return

    res = 1
    pre_nodes = 1
    for node_num in depth2num:
        if node_num == 0:
            print(0)
            return

        res *= pre_nodes**node_num
        res %= MOD
        pre_nodes = node_num
    print(res)

if __name__ == '__main__':
    main()