#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, factorial
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, M = map(int, input().split(' '))
    A = [list(map(int, input().split(' '))) for _ in range(M)]
    
    good_combi = set()
    for m in range(M):
        for n in range(N-1):
            x, y = A[m][n], A[m][n+1]
            if x > y:
                x, y = y, x
            good_combi.add((x, y))
    print((factorial(N)//(factorial(N-2)*factorial(2)))-len(good_combi))

if __name__ == '__main__':
    main()