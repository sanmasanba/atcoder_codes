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
    N = int(input())
    A = list(map(int, input().split(' ')))
    
    res = 0
    for i in range(len(A)-2):
        if A[i] == A[i+2]:
            res += 1

    print(res)

if __name__ == '__main__':
    main()