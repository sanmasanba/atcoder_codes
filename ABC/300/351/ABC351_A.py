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
    A = sum(list(map(int, input().split(' '))))
    B = sum(list(map(int, input().split(' '))))
    
    print(A-B+1)

if __name__ == '__main__':
    main()