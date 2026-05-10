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

#main
def main():
    N, X = map(int, input().split(' '))
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split(' '))
        A.append(a)
        B.append(b)
    
    res = INF
    sum_op_and_firstplay_time = 0
    min_stage_time = INF
    for i in range(N):
        sum_op_and_firstplay_time += A[i] + B[i]
        min_stage_time = min(min_stage_time, B[i])
        res = min(res, sum_op_and_firstplay_time + (X-1-i)*min_stage_time)
    print(res)

if __name__ == '__main__':
    main()