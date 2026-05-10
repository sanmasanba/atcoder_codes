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
    S, T = [], []
    for _ in range(N-1):
        s, t = map(int, input().split(' '))
        S.append(s)
        T.append(t)    
    for i in range(N-1):
        tmp = A[i]//S[i]
        A[i+1] += tmp * T[i]
    print(A[-1])
    

if __name__ == '__main__':
    main()