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
    N, T, P = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    
    res = 0
    while 1:
        cnt = 0
        for i in A:
            if i >= T:
                cnt += 1
        if cnt >= P:
            break
        res += 1
        for i in range(N):
            A[i] += 1

    print(res)

if __name__ == '__main__':
    main()