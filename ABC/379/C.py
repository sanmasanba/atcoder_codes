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
    N, M = map(int, input().split(' '))
    if M == 1:
        X = [int(input())]
        A = [int(input())]
        if X[0] != 1 or sum(A) != N:
            print(-1)
            return
        else:
            print(((N*(N-1))//2))
            return
    
    X = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' '))) 
    XA = [(X[i], A[i]) for i in range(M)]
    XA.sort()
    
    sum_val = 0
    sum_idx = 0
    for x, a in XA:
        # 今までにで石の数がxより小さい->ここまでたどり着けない
        if sum_val < x - 1:
            print(-1)
            return
        sum_val += a
        sum_idx += a*x

    if sum_val != N:
        print(-1)
        return
    
    # 操作が必要ないとき、石のあった位置の総和が(N*(N+1))//2
    # 操作が必要な時、石のあった位置の総和は小さくなる
    print((N*(N+1))//2 - sum_idx)

if __name__ == '__main__':
    main()