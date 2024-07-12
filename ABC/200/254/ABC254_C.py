#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    N, K = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = [[] for _ in range(K)]

    #Kごとに別々に収納
    for i in range(N):
        B[i%K].append(A[i])

    #それぞれをソートする
    A.sort()
    for i in range(K):
        B[i%K].sort(reverse=True)

    #順番に取り出す
    na = []
    for i in range(N):
        na.append(B[i%K].pop())

    if A == na:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()