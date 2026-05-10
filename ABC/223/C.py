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
    # 入力
    N = int(input())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split(' '))
        A.append(a)
        B.append(b)

    # 中点を求める
    half_t = 0
    res = 0
    for i in range(N):
        half_t += A[i]/B[i]
    half_t /= 2

    # シミュレーション
    for i in range(N):
        res += min(A[i], half_t*B[i])
        half_t -= min(A[i]/B[i], half_t)

    # 出力
    print(f"{res:.15f}")

if __name__ == '__main__':
    main()