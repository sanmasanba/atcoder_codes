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
    D, N = map(int, input().split(' '))
    if D == 0:
        if N != 100:
            print(N)
        else:
            print(101)
    else:
        if N != 100:
            print(N*(100**D))
        else:
            print(101*(100**D))

if __name__ == '__main__':
    main()