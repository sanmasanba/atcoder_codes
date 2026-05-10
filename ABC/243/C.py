#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import combinations

sys.setrecursionlimit(500000)
INF = float('inf')
NINF = -float('inf')

#main
def main():
    N = int(input())
    X, Y = [], []
    for _ in range(N):
        a, b = map(int, input().split(' '))
        X.append(a)
        Y.append(b)
    S = list(input())

    res = 'No'
    #右にむかう人たち、左に向かう人たち
    R, L = {}, {}
    for i in range(N):
        #もし右を向いていて
        if S[i] == 'R':
            #同じY軸の一番右端の人が左を向いていて、自分より右にいるなら
            if Y[i] in L and X[i] < L[Y[i]]:
                res = 'Yes'
                break
        #もし左を向いていて
        else:
            #同じY軸の一番左端の人が右を向いていて、自分より左にいるなら
            if Y[i] in R and R[Y[i]] < X[i]: 
                res = 'Yes'
                break

        #関係あるのは、一番端の人たちだけ
        if S[i] == 'R':
            #すでに同じY軸に人がいるとき
            if Y[i] in R:
                #自分と相手を比較して、より左にいるほうを選ぶ
                R[Y[i]] = min(R[Y[i]], X[i])
            #誰もいないなら、自分が代表
            else:
                R[Y[i]] = X[i]
        else:
            #すでに同じY軸に人がいるとき
            if Y[i] in L:
                #自分と相手を比較して、より右にいるほうを選ぶ
                L[Y[i]] = max(L[Y[i]], X[i])
            #誰もいないなら、自分が代表
            else:
                L[Y[i]] = X[i]

    print(res)

if __name__ == '__main__':
    main()