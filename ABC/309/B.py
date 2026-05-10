#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations
import copy

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N = int(input())
    A = [input() for _ in range(N)]
    B = copy.deepcopy(A)
 
    B[0] = A[1][0] + A[0][:-1]
    for i in range(1, N-1):
        B[i] = A[i+1][0] + A[i][1:-1] + A[i-1][-1]
    B[N-1] = A[N-1][1:] + A[N-2][-1]
    for b in B:
        print(b)

if __name__ == '__main__':
    main()