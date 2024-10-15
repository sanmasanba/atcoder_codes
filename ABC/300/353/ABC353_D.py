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
MOD = 998244353

#main
def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    cumsumA = [0]
    
    # 累積和
    for i in range(N):
        cumsumA.append(cumsumA[-1]+A[i])
    
    # 式変形する
    res = 0
    for i in range(1, N):
        order = len(str(A[i]))
        xs = (pow(10, order, MOD) * cumsumA[i])%MOD
        ys = (A[i] * i) % MOD
        res = (res + xs + ys) % MOD
    
    # output
    print(res)

if __name__ == '__main__':
    main()