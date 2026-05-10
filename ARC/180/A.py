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
    S = list(input())
    
    MOD = 1000000007
    left = 0
    right = 1
    res = 1

    while left < N:
        right = left + 1
        while right < N and S[right-1] != S[right]:            
            right += 1
        res = (res * ((right-left+1)//2))%MOD
        left = right

    print(res)

if __name__ == '__main__':
    main()