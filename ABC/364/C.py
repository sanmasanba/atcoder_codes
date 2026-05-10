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
    N, X, Y = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    A.sort(reverse=True)
    B.sort(reverse=True)

    res = INF
    sum_a = 0
    for i in range(N):
        sum_a += A[i]
        if sum_a > X:
            res = i
            break

    sum_b = 0
    for i in range(N):
        sum_b += B[i]
        if sum_b > Y:
            res = min(res, i)          
            break
    
    print(N if res==INF else res+1)
    
if __name__ == '__main__':
    main()