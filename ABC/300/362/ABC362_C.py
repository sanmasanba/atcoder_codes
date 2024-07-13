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
    L ,R = [], []
    for _ in range(N):
        l, r = map(int, input().split(' '))
        L.append(l)
        R.append(r)
    
    if 0 < sum(L) or sum(R) < 0:
        print('No')
    else:
        X = L.copy()
        sumX = sum(X)
        for i in range(N):
            # 増加分を考える
            # min(i番目の数字で増やせる最大値, 0と今の合計の差分)
            # ->どちらなら、現状の総和が0に近づくか
            d = min(R[i]-L[i], -sumX)
            sumX += d
            X[i] += d
        print('Yes')
        print(*X)

if __name__ == '__main__':
    main()