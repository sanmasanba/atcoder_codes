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
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split(' '))
        A.append(a)
        B.append(b)
    
    if sum(A) == sum(B):
        print('Draw')
    elif sum(A) > sum(B):
        print('Takahashi')
    else:
        print('Aoki')

if __name__ == '__main__':
    main()