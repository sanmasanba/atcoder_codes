#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

from string import ascii_lowercase

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    N = int(input())
    S = input()
    Q = int(input())
    # a-zまでの文字列で初期化
    map_from = ascii_lowercase
    map_to = ascii_lowercase

    # クエリを使って、変化後の文字列を生成する
    for _ in range(Q):
        c, d = input().split(' ')
        map_to = map_to.replace(c, d)

    # maketransを用いてmap_fromとmap_toで辞書型を作成
    print(S.translate(str.maketrans(map_from, map_to)))

if __name__ == '__main__':
    main()