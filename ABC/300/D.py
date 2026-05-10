#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations, accumulate

sys.setrecursionlimit(10**6)
INF = float('inf')
def eratosthenes(N):
    isprime = [True] * (N+1)

    isprime[0], isprime[1] = False, False

    for p in range(2, N+1):
        if not isprime[p]:
            continue

        q = p * 2
        while q <= N:
            isprime[q] = False
            q += p

    return [i for i, e in enumerate(isprime) if e]

#main
def main():
    # input
    N = int(input())

    prime_nums = eratosthenes(10**6)
    P = len(prime_nums)
    res = 0
    for i in range(P-2):
        a = prime_nums[i]
        for j in range(i+2, P):
            c = prime_nums[j]
            r = (a**2)*(c**2)
            if N < r:
                break
            # binary search left
            low = i
            high = j
            while low+1 < high:
                mid = (high+low)//2
                n = r * prime_nums[mid]
                if n > N:
                    high = mid
                else:
                    low = mid
            res += low-i
    
    # output
    print(res)

if __name__ == '__main__':
    main()