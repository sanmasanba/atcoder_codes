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
    N = int(input())
    Q = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    
    A_nums = [q//a if a else INF for q, a in zip(Q, A)]
    A_min = min(A_nums)
    Q_A = [q-a*A_min for q, a in zip(Q, A)]
    B_nums = [q//b if b else INF for q, b in zip(Q_A, B)]
    B_min = min(B_nums)
    res = A_min+B_min

    while A_min > 0:
        A_min -= 1
        Q_A = [q-a*A_min for q, a in zip(Q, A)]
        B_nums = [q//b if b else INF for q, b in zip(Q_A, B)]
        B_min = min(B_nums)     
        res = max(res, A_min+B_min)
    print(res)

if __name__ == '__main__':
    main()