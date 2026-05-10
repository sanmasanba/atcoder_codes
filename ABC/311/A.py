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
    a, b, c = 0, 0, 0
    for i in range(N):
        if S[i] == 'A':
            a = 1
        if S[i] == 'B':
            b = 1
        if S[i] == 'C':
            c = 1
        if a == 1 and b == 1 and c == 1:
            print(i+1)
            break 

if __name__ == '__main__':
    main()