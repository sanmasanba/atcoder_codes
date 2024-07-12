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
    S = input()
    
    #今の数字を起点に左に来るもの
    L = []
    #今の数字を起点に右に来るもの(反転して持つ)
    R = []

    #i+1を
    for i, s in enumerate(S):
        #左に挿入するから
        if s=='L':
            #iは右に入る(例：1を左挿入するとき、0は右に行く -> 1, 0)
            R.append(i)
        #右に挿入するなら
        else:
            #iは左に入る(例：1を右挿入するとき、0は左に行く -> 0, 1)
            L.append(i)

    print(*(L+[N]+R[::-1]))

if __name__ == '__main__':
    main()