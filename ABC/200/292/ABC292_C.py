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
solver_set = {}
#solver : O(√N)
def solver(N) -> list:
    if N in solver_set:
        return solver_set[N]
    res = 0
    for p in range(1, N+1):
        if p * p > N:
            break
        if N % p != 0:
            continue
        if p**2 == N:
            res += 1
        else:
            res += 2
    solver_set[N] = res
    return res

#main : O(n√N)
def main():
    N = int(input())
    res = 0
    # 積ABが1~N-1まで推移することを考える
    for AB in range(1, N//2+1):
        # 積CDはN-ABになる
        CD = N - AB
        if 2*AB == N:
            res += solver(AB)*solver(CD)
        else:    
            res += 2*solver(AB)*solver(CD)
    print(res)

if __name__ == '__main__':
    main()
    