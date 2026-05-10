#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    # input
    N, Q = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    
    # 累積和を用いて、操作が必要な点のパターン分けをする
    A.sort()
    cumsumA = [0]
    for i in range(N):
        cumsumA.append(cumsumA[-1] + A[i])
    res = []
    for _ in range(Q):
        x = int(input())
        left = bisect_left(A, x)
        right = bisect_right(A, x)
        left_cumsum = cumsumA[left]-cumsumA[0]
        if N <= right:
            right_cumsum = 0
            right = 0
        else:
            right_cumsum = cumsumA[-1] - cumsumA[right]
            right = N - right
        res.append((x*left - left_cumsum) + (right_cumsum - x*right))
    
    # output
    print(*res, sep='\n')

if __name__ == '__main__':
    main()