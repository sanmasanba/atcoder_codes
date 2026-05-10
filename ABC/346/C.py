#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    N, K = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    A_set = set(A)

    sums = (K * (K + 1)) // 2
    suma = 0
    for a in A_set:
        if a <= K:
            suma += a

    print(sums - suma)

if __name__ == '__main__':
    main()