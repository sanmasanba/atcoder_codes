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
    # input
    N, K = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    
    # 前からと後ろからの奇妙さを計算しておく
    # pre[0]:=(2-1)
    # pre[1]:=(4-3)+(2-1) 
    pre = [0] * (K+1)
    # suf[0]:=(K-(K-1))
    # suf[0]:=((K-2)-(K-3))+(K-(K-1))
    suf = [0] * (K+1)
    for i in range(1, K+1):
        pre[i] = pre[i-1]
        if i%2 == 0:
            pre[i] += A[i-1] - A[i-2]
    for i in range(K-1, -1, -1):
        suf[i] = suf[i+1]
        if (K-i)%2 == 0:
            suf[i] += A[i+1] - A[i]

    res = INF
    for i in range(0, K+1, 2):
        res = min(res, pre[i]+suf[i])

    # output
    print(res)

if __name__ == '__main__':
    main()