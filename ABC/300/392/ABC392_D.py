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
    N = int(input())
    As = []
    for _ in range(N):
        _, *A = map(int, input().split())
        A_num = len(A)
        A = Counter(A)
        As.append((A_num, A))
    
    res = 0
    for a, b in combinations(As, 2):
        A_num, A = a
        B_num, B = b
        all = A_num*B_num
        cnt = 0
        for k, v in A.items():
            cnt += v*B.get(k, 0)
        res = max(res, (cnt*(10**9))/all)
    
    print(res if not res else res/10**9)

if __name__ == '__main__':
    main()