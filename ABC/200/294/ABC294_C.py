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
    N, M = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    
    A_res, B_res = [], []
    a_pos, b_pos = 0, 0
    for i in range(1, N+M+1):
        if N <= a_pos:
            B_res.append(i)
            continue
        if M <= b_pos:
            A_res.append(i)
            continue
        if A[a_pos] < B[b_pos]:
            A_res.append(i)
            a_pos += 1
        else:
            B_res.append(i)
            b_pos += 1

    print(*A_res)
    print(*B_res)

if __name__ == '__main__':
    main()