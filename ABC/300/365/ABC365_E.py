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
    
    res = 0
    for i in range(N-1):
        tmp =  A[i]
        for j in range(i+1, N):
            tmp ^= A[j]
            res += tmp
    print(res)

if __name__ == '__main__':
    main()