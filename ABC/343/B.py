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
    A = [list(map(int, input().split(' '))) for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
                if A[i][j] == 1:
                    print(j+1, end=' ')
        print('')

if __name__ == '__main__':
    main()