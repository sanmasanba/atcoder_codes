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

class BIT:
    def __init__(self, n: int):
        self.n = n+1
        self.L = [0]*self.n
    
    def add(self, idx: int, val: int):
        """１点加算

        Args:
            idx (int): 1-indexed
            val (int): 加算する値
        """
        while idx < self.n:
            self.L[idx] += val
            idx += (idx & -idx)
    
    def sum(self, idx: int) -> Any:
        """区間取得

        Args:
            idx (int): 1-indexed

        Returns:
            Any: 区間和
        """
        res = 0
        while idx > 0:
            res += self.L[idx]
            idx -= (idx & -idx)
        return res

#main
def main():
    # intput
    N = int(input())
    P = [(int(p), i+1) for i, p in enumerate(input().split())]
    A = [-1]*N
    memo = BIT(N)
    for i in range(1, N+1): memo.add(i, 1)

    while P:
        p, i = P.pop()
        low = 1
        high = N
        while low < high:
            mid = (low + high) // 2
    
            if memo.sum(mid) < p:
                low = mid + 1
            else:
                high = mid
        A[low-1] = i
        memo.add(low, -1)

    print(*A)

if __name__ == '__main__':
    main()