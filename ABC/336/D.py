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

#main
def main():
    N = int(input())
    A = [0] + list(map(int, input().split(' ')))
    
    # ピラミッド数列 = [1, 2, ..., K-1, K, K-1, ..., 2, 1]としたとき
    # [1, 2, ..., K-1, K] := 左ピラミッド数列
    # [K, K-1, ..., 2, 1] := 右ピラミッド数列
    # としたとき、Aiを右端あるいは左端とするときの数列の長さをli, riとする
    l, r  = [0] * (N+2), [0] * (N+2)
    for i in range(1, N+1):
        # l0 = 0としたとき、li = min(Ai, li-1 + 1)が成り立つ
        # -> Ai-1までを使った時の高さがtの時、Aiを右端とする左ピラミッド数列は
        #    0 < li <= t+1 となる。
        l[i] = min(A[i], l[i-1]+1)
    for i in range(N, 0, -1):
        # 左ピラミッド数列と同様に求めることができる
        r[i] = min(A[i], r[i+1] + 1)
    # Aiを頂点とするピラミッド数列は、min(li, ri)となる
    print(max(min(l[i], r[i]) for i in range(1, N+1)))            

if __name__ == '__main__':
    main()