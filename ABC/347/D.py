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
    a, b, C = map(int, input().split(' '))

    A = []
    B = []
    a_num, b_num = a, b
    for i in range(60):
        ci =( C >> 59-i) & 1

        if ci:
            if a_num < b_num and 0 < b_num:
                A.append('0')
                B.append('1')
                b_num -= 1
            elif b_num <= a_num and 0 < a_num:
                A.append('1')
                B.append('0')
                a_num -= 1
            else:
                print(-1)
                return
        else:
                A.append('-1')
                B.append('-1')

    if a_num != b_num:
        print(-1)
        return

    for i in range(60):
        if A[i] == '-1':
            if 0 < a_num:
                A[i] = '1'
                B[i] = '1'
                a_num -= 1
            else:
                A[i] = '0'
                B[i] = '0'
    
    if 0 < a_num:
        print(-1)
        return
    
    print(int("".join(A), 2), int("".join(B), 2))

if __name__ == '__main__':
    main()