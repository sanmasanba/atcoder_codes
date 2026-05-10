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
    P = list(map(int, input().split(' ')))

    # P_j > P_j+1 < P_j+2, P_j+3, ..., P_Nとなるjを探す
    j = N - 2
    while P[j] < P[j+1]:
        j -= 1

    # j+1番目以降で、P_jより小さくて、最大の要素を探す
    k = N - 1
    while P[j] < P[k]:
        k -= 1
    
    # P_jはP_kとなる必要がある
    P[j], P[k] = P[k], P[j]
    print(*P[:j+1], *P[:j:-1])

if __name__ == '__main__':
    main()