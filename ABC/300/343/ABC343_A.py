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
    A, B = map(int, input().split(' '))
    for i in range(10):
        if A + B != i:
            print(i)
            break

if __name__ == '__main__':
    main()