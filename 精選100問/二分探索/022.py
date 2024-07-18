#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

def func(x, P):
    return x + P/(2**(x/1.5))

#main
def main():
    P = float(input())
    #最大と最小の設定
    low = 0
    high = 1 << 8
    while low >= 0 and high-low > 0.000000001:
        #中間点の設定
        mid = (low + high) / 2
        # 勾配を求める
        d = (func(mid+0.00001, P)-func(mid, P))/(0.00001)

        # 勾配がほぼ0に収束したら答え
        if 0 < abs(d) < 0.000000001:
            break
        # 勾配が正のとき、極限はまだ左にある
        if d > 0:
            high = mid
        # 勾配が正のとき、極限はまだ右にある
        else:
            low = mid
    print(func(mid, P))

if __name__ == '__main__':
    main()