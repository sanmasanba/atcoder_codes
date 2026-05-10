#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    X, A, D, N = map(int, input().split(' '))
    if D == 0:
        print(abs(X-A))
    else:
        l, u = floor((X-A)/D), ceil((X-A)/D)
        if u < 0:
            print(abs(X-A))
        elif N-1 < l:
            print(abs(X-(A+D*(N-1))))
        else:
            print(min(abs(X-(A+D*u)), abs(X-(A+D*l))))

if __name__ == '__main__':
    main()