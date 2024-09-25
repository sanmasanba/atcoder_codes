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
    N = int(input())
    A = list(map(int, input().split(' ')))
    
    res = []
    for i in range(N-1):
        if abs(A[i]-A[i+1]) < 2:
            res.append(A[i])
        elif A[i] < A[i+1]:
            res += [i for i in range(A[i], A[i+1])]
        else:
            res += [i for i in range(A[i], A[i+1], -1)]

    print(*res+[A[-1]])

if __name__ == '__main__':
    main()