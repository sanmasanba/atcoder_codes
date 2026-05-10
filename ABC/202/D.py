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
    A, B, K = map(int, input().split(' '))
    idx = 1
    if K == 1:
        print('a'*A + 'b' * B)
        return
    
    memo = [0] * 61
    memo[0] = 1
    for i in range(1, 61):
        memo[i] = memo[i-1] * i

    res = [None] * (A + B)
    idx = 0
    for _ in range(A+B):
        if A == 0 or B == 0:
            if A:
                print('a'*A)
            else:
                print('b'*B)
            break
        tmp = memo[A+B-1]//(memo[A-1]*memo[B])
        if K <= idx + tmp:
            A -= 1
            print('a', end='')
        else:
            idx += tmp
            B -= 1
            print('b', end='')

if __name__ == '__main__':
    main()