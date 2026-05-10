#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul, xor, or_
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
    A = list(map(int, input().split(' ')))
    
    res = INF
    for bit in range(2**(N)):
        partition = [0]
        for mask in range(1, N):
            if bit >> mask & 1:
                partition.append(mask)
        if not partition or partition[-1] != N:
            partition.append(N)
        arr = []
        if len(partition) == 1:
            res = min(res, reduce(or_, A))
        else:
            for i in range(len(partition)-1):
                arr.append(reduce(or_, A[partition[i]:partition[i+1]]))
            res = min(res, reduce(xor, arr))
    
    # output
    print(res)

if __name__ == '__main__':
    main()