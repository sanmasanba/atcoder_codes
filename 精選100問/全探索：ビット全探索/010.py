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
    N = int(input())
    A = list(map(int, input().split(' ')))
    q = int(input())
    Ms = list(map(int, input().split(' ')))
    
    for m in Ms:
        #bit_search
        res = 'no'
        if sum(A) < m:
            pass
        else:
            for i in range(2**N):
                total = 0
                for j in range(N):
                    if (i >> j) & 1:
                        total += A[j]
                if total == m:
                    res = 'yes'
                    break
        print(res)

if __name__ == '__main__':
    main()