#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, Q = map(int, input().split(' '))
    S = list(input())
    L, R = [], []
    for _ in range(Q):
        a, b = map(int, input().split(' '))
        L.append(a)
        R.append(b)
    A_check = [0 for _ in range(300010)]
    B_check = [0 for _ in range(300010)]
    # それぞれの文字をみていき、同じ文字が2文字連続なら1
    for i in range(1, N): A_check[i] = 1 if S[i-1] == S[i] else 0
    # 1文字目からi文字目までの条件を満たすペアの数はA_checkの累積和になる
    for i in range(1, N): B_check[i] = B_check[i-1] + A_check[i]

    #条件を満たすのは、B_chack[1:r-1]-B[1:l-1]になる(累積和の特性)
    for l, r in zip(L, R):
        print(B_check[r-1]-B_check[l-1])

if __name__ == '__main__':
    main()