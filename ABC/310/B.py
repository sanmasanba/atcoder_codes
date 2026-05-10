#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, M = map(int, input().split(' '))
    P, C, F = [], [], []
    for _ in range(N):
        PCF = list(map(int, input().split(' ')))
        P.append(PCF[0])
        C.append(PCF[1])
        F.append(set(PCF[2:]))
    res = False
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if P[i] >= P[j] and F[j] >= F[i] and (P[i] > P[j] or len(F[j]-F[i])):
                res = True
    print('Yes' if res else 'No')

if __name__ == '__main__':
    main()