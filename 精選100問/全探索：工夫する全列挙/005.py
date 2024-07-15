#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    A, B, C, X, Y = map(int, input().split(' '))
    AB = min(X, Y)

    ABs = (A+B)*AB
    Cs = 2*C*AB
    res_ABs = A*max(X-AB, 0) + B*max(Y-AB, 0) + ABs
    res_Cs = A*max(X-AB, 0) + B*max(Y-AB, 0) + Cs
    print(min(res_ABs, res_Cs, 2*C*max(X, Y)))

if __name__ == '__main__':
    main()