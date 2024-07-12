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
    N, T = map(int, input().split(' '))
    S = list(input())
    X = list(map(int, input().split(' ')))
    
    x1, x2 = [], []
    for i, s in enumerate(S):
        #正方向に向かうリスト
        if s == '1':
            x1.append(X[i])
        #負方向に向かうリスト
        else:
            x2.append(X[i])
    
    x1.sort()
    x2.sort()
    
    #尺取り法
    l, r = 0, 0
    res = 0
    x1size = len(x1)
    x2size = len(x2)
    for i in range(x1size):
        #負の方向に向かう蟻が、正の方向に向かう蟻よりもマイナス側ならインクリメント
        while l < x2size and x2[l] < x1[i]:
            l += 1
        #rは右に向かう蟻から２Tまでの位置までしか考えない
        while r < x2size and x2[r] <= x1[i] + 2*T:
            r += 1

        #print(r, l)
        res += r - l 

    print(res)

if __name__ == '__main__':
    main()