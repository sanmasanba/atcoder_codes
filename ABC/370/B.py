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
    A = []
    for _ in range(N):
        a = list(map(lambda x: int(x)-1, input().split(' ')))
        A.append(a)

    i=0
    for j in range(N):
        if i >= j:
            i = A[i][j]
        else:
            i = A[j][i]
    print(i+1)

if __name__ == '__main__':
    main()