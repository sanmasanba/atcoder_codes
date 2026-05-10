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
def left(p, N, M):
    res = set()
    i = 0
    while (p-i+N)%N != M:
        res.add((p-i+N)%N)
        i += 1
    return res

def right(p, N, M):
    res = set()
    i = 0
    while (p+i+N)%N != M:
        res.add((p+i+N)%N)
        i += 1
    return res

#main
def main():
    N, Q = map(int, input().split(' '))
    l = 0; r = 1
    res = 0
    for _ in range(Q):
        H, M = input().split(' ')
        M = int(M)-1

        match H:
            case 'L':
                left_move = left(l, N, M)
                right_move = right(l, N, M)
                if r in left_move:
                    res += len(right_move)
                else:
                    res += len(left_move)
                l = M
            case 'R':
                left_move = left(r, N, M)
                right_move = right(r, N, M)      
                if l in left_move:
                    res += len(right_move)
                else:
                    res += len(left_move)
                r = M
    print(res)

if __name__ == '__main__':
    main()