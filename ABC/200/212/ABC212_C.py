#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')
def f(a, b):
    return abs(a-b)

#main
def main():
    # input
    N, M = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    A.sort()
    B.sort()

    res = INF
    for a in A:
        if M == 1:
            res = min(res, f(a, B[0]))
            continue
        insert_pos = bisect_left(B, a)
        if insert_pos == 0:
            res = min(res, f(a, B[insert_pos]))
        elif 0 < insert_pos < M-1:
            res = min(res, f(a, B[insert_pos]), f(a, B[insert_pos-1]))
        else:
            res = min(res, f(a, B[insert_pos-1]))
        
    print(res)

if __name__ == '__main__':
    main()