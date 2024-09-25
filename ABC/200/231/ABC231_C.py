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
    N, Q = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    A.sort()

    res = []
    for _ in range(Q):
        x = int(input()) 
        res.append(N-bisect_left(A, x))
    print(*res, sep='\n')

if __name__ == '__main__':
    main()