#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')
MOD = 100000000

#main
def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    A.sort()

    cnt = 0
    right = N
    for left in range(N):
        right = max(right, left+1)
        while left < right-1 and MOD <= A[right-1] + A[left]:
            right -= 1
        cnt += N - right

    res = 0
    for i in range(N):
        res += (N-1)*A[i]
    print(res - cnt*MOD)

if __name__ == '__main__':
    main()