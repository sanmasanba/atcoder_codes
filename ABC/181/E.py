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
    H = list(map(int, input().split()))
    W = list(map(int, input().split()))
    H.sort()

    even = [abs(H[i]-H[i+1]) for i in range(0, N-1, 2)]
    odd = [abs(H[i]-H[i+1]) for i in range(1, N, 2)]
    cumsum_even = [0] + list(accumulate(even))
    cumsum_odd = [0] + list(accumulate(odd))

    res = INF
    for w in W:
        idx = bisect_left(H, w)
        l = idx//2
        left_sum = cumsum_even[l]
        if not idx%2:
            if idx < N:
                sub = abs(w-H[idx])
            else:
                sub = abs(w-H[-1])
        else:
            sub = abs(w-H[idx-1])
        right_sum = cumsum_odd[-1] - cumsum_odd[idx//2]
        res = min(res, left_sum + sub + right_sum)
    print(res)

if __name__ == '__main__':
    main()