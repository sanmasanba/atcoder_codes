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
    A, S = [], []
    l, r = 0, 0
    for _ in range(N):
        a, b = input().split(' ')
        a = int(a)
        if l == 0 and b == "L":
            l = a
        if r == 0 and b == "R":
            r = a
        A.append(a)
        S.append(b)
    
    res = 0
    for a, s in zip(A, S):
        if s == 'L':
            res += abs(l-a)
            l = a
        else:
            res += abs(r-a)
            r = a
    print(res)    

if __name__ == '__main__':
    main()