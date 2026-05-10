#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, List, Tuple, Dict, TypeVar, Optional
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    # input
    N = int(input())
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    # 貪欲に大きいほうから入れて、2回購入したら終わり
    res = -1
    b = 0
    for i in range(N):
        if b == N-1:
            print(A[-1])
            return
        if A[i] > B[b]:
            if res != -1:
                print(-1)
                return
            else:
                res = A[i]
                b -= 1
        b += 1
    
    # output
    print(res)

if __name__ == '__main__':
    main()