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
import math

#main
def main():
    # intput
    N, K, P = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    
    if K == 1 or N == 1:
        print(len([i for i in A if i <= P]))
        return
    
    # 半分全列挙をする
    set_top = [[] for _ in range(N+1)]
    set_tail = [[] for _ in range(N+1)]
    
    # 前半
    for bit in range(2**(N//2)):
        total = 0
        cnt = 0
        for k in range(N):
            if bit >> k & 1:
                total += A[k]
                cnt += 1
        set_top[cnt].append(total)
    # 後半
    for bit in range(2**(N - N//2)):
        total = 0
        cnt = 0
        for k in range(N - N//2):
            if bit >> k & 1:
                total += A[N//2 + k]
                cnt += 1
        set_tail[cnt].append(total)
    for i in range(len(set_tail)): set_tail[i] = sorted(set_tail[i]) 

    res = 0
    for k1, k_set in enumerate(set_top):
        k2 = K - k1
        while k_set:
            p1 = k_set.pop()
            p2 = P - p1
            if 0 <= p2:
                cnt = bisect_right(set_tail[k2], p2)
                if cnt is not None:
                    res += cnt
    print(res)

if __name__ == '__main__':
    main()