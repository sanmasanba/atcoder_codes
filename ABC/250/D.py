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
# 1 以上 N 以下の整数が素数かどうかを返す
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
    N = int(input())
    res = 0
    eratosthenes = Eratosthenes(10**6)
    for q in eratosthenes:
        # q**3がNを超えたら終わり
        if N < q ** 3:
            break
        # pの上限 floor(N/(q**3))
        p = N // (q ** 3)
        if p < 2:
            break
        if p < q:
            p_cnt = bisect_left(eratosthenes, p)
            if eratosthenes[p_cnt] == p:
                p_cnt += 1
        else:
            p_cnt = bisect_left(eratosthenes, q-1)
            if eratosthenes[p_cnt] == q-1:
                p_cnt += 1
        res += p_cnt

    print(res)

if __name__ == '__main__':
    main()