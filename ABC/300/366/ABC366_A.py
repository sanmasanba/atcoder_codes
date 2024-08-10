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
    N, T,  A = map(int, input().split(' '))
    print("Yes" if floor(N/2) < T or floor(N/2) < A else 'No')

if __name__ == '__main__':
    main()