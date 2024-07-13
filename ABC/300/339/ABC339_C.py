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
    
    s = [0]
    for a in A:
        s.append(s[-1]+a)
    print(s[-1]-min(s))

if __name__ == '__main__':
    main()