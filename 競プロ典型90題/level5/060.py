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

def LIS(A: List[int]):
    N = len(A)
    dp = [A[0]]
    res = [0] * N
    for i in range(N):
        if A[i] > dp[-1]:
            dp.append(A[i])
            res[i] = len(dp)
        else:
            pos = bisect_left(dp, A[i])
            dp[pos] = A[i]
            res[i] = pos + 1
    return res

#main
def main():
    # intput
    N = int(input())
    A = list(map(int, input().split(' ')))
    
    from_left = LIS(A)
    A = list(reversed(A))
    from_right = LIS(A)
    from_right = list(reversed(from_right))

    res = 0
    for i in range(N):
        res = max(res, from_left[i] + from_right[i] - 1)
    print(res)

if __name__ == '__main__':
    main()