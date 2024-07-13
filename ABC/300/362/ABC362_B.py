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
    X, Y = [], []
    for _ in range(3):
        x, y = map(int, input().split(' '))
        X.append(x)
        Y.append(y)
    a = (X[0]-X[1])**2+(Y[0]-Y[1])**2
    b = (X[1]-X[2])**2+(Y[1]-Y[2])**2
    c = (X[2]-X[0])**2+(Y[2]-Y[0])**2

    print('Yes' if max(a, b, c) == (a+b+c-max(a, b, c)) else 'No')

if __name__ == '__main__':
    main()