#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    D = int(input())
    ans = D
    for x in range(int(sqrt(D)) + 9):
        # 仮のｙの二乗を仮定する
        z = D - x * x
        # x座標が、円の軌道より外側の時
        if z < 0:
            ans = min(ans, -z)
        # 円の軌道を挟む点二つを求める
        else:
            y1 = int(sqrt(z))
            y2 = y1 + 1
            ans = min(ans, z-y1*y1, y2*y2-z)
    print(ans)

if __name__ == '__main__':
    main()