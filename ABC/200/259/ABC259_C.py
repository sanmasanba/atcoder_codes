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
    S = list(input())
    T = list(input())

    S_N = len(S)
    T_N = len(T)

    sright = 0   
    sleft = 0
    tright = 0  
    tleft = 0
    res = 'Yes'
    while sright < S_N and tright < T_N:
        #S側の連続する文字列の長さを数える
        slen = 0
        while sright < S_N and S[sleft] == S[sright]:
            sright += 1

        slen = sright - sleft
        sleft = sright
        s = S[sright-1]

        #T側の連続する文字列の長さを数える
        tlen = 0
        while tright < T_N and T[tleft] == T[tright]:
            tright += 1

        tlen = tright - tleft
        tleft = tright
        t = T[tright-1]

        if (s != t) or (slen < tlen and slen == 1) or slen > tlen:
            res = 'No'
            break

    if res != 'No' and (sright != S_N or tright != T_N):
        res = 'No'

    print(res)

if __name__ == '__main__':
    main()