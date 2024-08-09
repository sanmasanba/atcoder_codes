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
    N, H, X = map(int, input().split(' '))
    P = list(map(int, input().split(' ')))
    
    for n in range(N):
        if X <= H+P[n]:
            print(n+1)
            break

if __name__ == '__main__':
    main()