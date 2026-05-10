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
    Sx, Sy = map(int, input().split(' '))
    Tx, Ty = map(int, input().split(' '))
    
    #左にそろえる
    # y軸とx軸で座標が同じとき左にあるので、差の偶奇を判定すれば左にあるかわかる
    # (偶数, 偶数) ⇒左にある。常に偶数
    # (偶数, 奇数) ⇒右にある。常に奇数
    # (奇数, 偶数) ⇒右にある。常に奇数
    # (奇数, 奇数) ⇒左にある。常に偶数
    # 奇数 % 2 = 1　なので以下のような実装で左にずらせる。
    Sx -= (Sy - Sx) % 2
    Tx -= (Ty - Tx) % 2

    # スタート地点の座標を引いている
    # ⇒スタート地点を(0, 0)に移動している
    Tx -= Sx
    Ty -= Sy

    #移動距離
    Tx = abs(Tx)
    Ty = abs(Ty)

    # (右上方向の移動＋max(0, X軸方向の移動ー右上方向の移動)/2）
    # = (右上方向の移動 + (目標が自身より左なら０で、２マスごとなので2で割る))
    print(Ty + max(0, Tx - Ty) // 2)

if __name__ == '__main__':
    main()