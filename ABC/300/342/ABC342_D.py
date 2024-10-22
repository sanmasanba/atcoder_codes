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

#prime_factorization
def prime_factorization(N) -> list:
    res = 1
    for p in range(2, N):
        if p * p > N:
            break
        if N % p != 0:
            continue
        e = 0
        while N % p == 0:
            e += 1
            N //= p
        if e%2:
            res *= p
    if N != 1:
        res *= N
    return res

#main
def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    
    primes = [0] * (2*10**5+1)
    for a in A:
        if a == 0:
            primes[a] += 1
            continue    
        a = prime_factorization(a)
        primes[a] += 1

    res = 0
    for prime in range(2*10**5+1):
        primenum_cnt = primes[prime]
        if prime == 0:
            res += primenum_cnt*N - ((primenum_cnt+1)*primenum_cnt)//2 
            continue
        if primenum_cnt < 2:
            continue
        res += ((primenum_cnt-1)*primenum_cnt)//2
    
    print(res)

if __name__ == '__main__':
    main()