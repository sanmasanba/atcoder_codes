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
    A = [list(input()) for _ in range(N)]
    B = [list(input()) for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if A[i][j] != B[i][j]:
                print(i+1, j+1)
                sys.exit(0)

if __name__ == '__main__':
    main()