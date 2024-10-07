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
def Eratosthenes(N):
    # テーブル
    isprime = [True] * (N+1)

    # 0, 1 は予めふるい落としておく
    isprime[0], isprime[1] = False, False

    # ふるい
    for p in range(2, N+1):
        # すでに合成数であるものはスキップする
        if not isprime[p]:
            continue

        # p 以外の p の倍数から素数ラベルを剥奪
        q = p * 2
        while q <= N:
            isprime[q] = False
            q += p

    # 1 以上 N 以下の整数が素数かどうか判定して素数のリストを返す
    return [i for i, e in enumerate(isprime) if e]

#main
def main():
    A, B, C, D = map(int, input().split(' '))
    eratosthenes = set(Eratosthenes(300))

    res = True
    for takahashi_choice in range(A, B+1):
        this_choice_res = False
        for aoki_choice in range(C, D+1):
            this_choice_res |= (takahashi_choice + aoki_choice) in eratosthenes
        res &= this_choice_res
    print('Aoki' if res else 'Takahashi')

if __name__ == '__main__':
    main()